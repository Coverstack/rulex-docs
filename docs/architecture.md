# Architecture

> This page covers the internals of RuleX. It is intended for a technical audience.

## Build pipeline

When a **[Data Source](concepts/data-sources.md)** is uploaded, RuleX transpiles the Excel formulas into Rust source code, which is then compiled into a WebAssembly module. This module is compiled Ahead-of-Time (AOT) into a native executable for each supported target architecture (`x86_64-linux`, `aarch64-linux`).

![Build pipeline](assets/diagrams/rulex-build-pipeline-light.svg#only-light){ .center }
![Build pipeline](assets/diagrams/rulex-build-pipeline-dark.svg#only-dark){ .center }

**[Endpoints](concepts/endpoints.md)** depend on this executable. Until compilation is complete, an Endpoint returns HTTP 404.

!!! note
    In [demo.rulex.coverstack.in](https://demo.rulex.coverstack.in/), only WebAssembly modules are generated.
    Executables are compiled on demand when you **[self-host](self-hosting/running-the-server.md#on-demand-compilation)**.

## Request-response cycle

Once the executable is ready, each request follows this flow:

![Request-response cycle](assets/diagrams/rulex-request-flow-light.svg#only-light){ .center }
![Request-response cycle](assets/diagrams/rulex-request-flow-dark.svg#only-dark){ .center }

Each request is authenticated and validated against the configured **[Schema](concepts/endpoint-schemas.md)**. Failures are rejected immediately.
Passing requests are sent to the runtime: inputs are fed in, outputs are read out, and the result is translated into an HTTP response.

## Runtime

The runtime is powered by [rulex-runtime](https://pypi.org/project/rulex-runtime/), a Rust extension built on [Wasmer](https://wasmer.io) with the LLVM compiler backend.
It manages the lifecycle of WebAssembly instances, an LRU cache of recently used modules, and a thread pool for concurrent execution.

[rulex-runtime](https://pypi.org/project/rulex-runtime/) is the package that powers **[Self Hosting](self-hosting/running-the-server.md)**.
It is included as a dependency in **[rulex.zip](self-hosting/running-the-server.md#using-rulexzip-as-a-library)**.

### Caching hints

Each calculation returns a caching hint alongside its output. RuleX uses this to determine whether a response can be cached and for how long:

| Hint | Meaning |
|------|---------|
| `Forever` | Output depends only on the inputs. Safe to cache indefinitely. |
| `Today` | Output depends on the current date (e.g. a model using `TODAY()`). Safe to cache until midnight. |
| `Never` | Output depends on a volatile function such as `NOW()` or `RAND()`. Must not be cached. |

RuleX uses this hint internally to cache results in full access mode. The self-hosted server does not implement caching.

### Concurrency

Each call to the executable is fully isolated and concurrent requests do not share state.
The runtime releases Python's Global Interpreter Lock (GIL) before acquiring a thread slot, so multiple calculations run in parallel on separate OS threads.

When self-hosting, configure concurrency no higher than the number of physical CPU cores on the host.
