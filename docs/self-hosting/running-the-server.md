# Running the Server

The exported ZIP includes a ready-to-run HTTP server. This page explains how to start
it and what to expect.

## Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) on your server.

## Starting the server

Extract the ZIP and run:

```bash
uv run server.py
```

The server starts on port 8000. Visit `http://localhost:8000/docs` for the Swagger UI,
where you can explore and test the exported **[Endpoints](../concepts/endpoints.md)**.

## On-demand compilation

If the endpoints are exported from [demo.rulex.coverstack.in](https://demo.rulex.coverstack.in),
the ZIP does not contain the executables. On the first request to an Endpoint, the server
compiles the module into a native executable for your CPU architecture in the
background. While compilation is running, the Endpoint returns HTTP 503. Once complete,
it responds normally.

To avoid this cold start, you can precompile Endpoints at startup. See `README.md`
inside `rulex.zip` for details.

## Using rulex.zip as a library

`rulex.zip` is also a Python package. If you do not need the HTTP server, you can use
it directly in your own application.

Add it to your dependencies:

```
# requirements.txt
rulex.zip
```

Or

```bash
uv add rulex.zip
```

Instructions and the full API reference are in `README.md` inside `rulex.zip`.

## Supported platforms

`rulex.zip` supports `x86_64-linux` and `aarch64-linux`.
Running the server or library usage on other platforms is not currently supported.
