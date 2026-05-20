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

Each request is authenticated and validated against the configured **[Schema](concepts/endpoint-schemas.md)**. Failures are rejected immediately. Passing requests are sent to the executable: inputs are fed in, outputs are read out, and the result is translated into an HTTP response.
