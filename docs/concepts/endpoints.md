# Endpoints

An Endpoint is a URL path backed by an **[Endpoint Schema](endpoint-schemas.md)**. Calling the Endpoint URL runs
the Excel model and returns the outputs.

You can define multiple Endpoints for a single **[Schema](endpoint-schemas.md)**. This is useful when you want
to serve the same model at different paths or with different configurations.

## URL path

The path starts with `/` and must not contain URL-escapable characters. For example,
`/calculate/price` is valid, but `/calculate/price?v=1` is not.

Paths are unique across your Organisation. No two Endpoints can share the same path.

## Modes

An Endpoint can operate in two modes, either independently or at the same time:

- **JSON API:** accepts `POST` requests from any HTTP client. Requires an **[API Config](../configuring/api-config.md)**
  (which provides the API key).
- **Web Form:** renders an HTML form in the browser. Requires a **[Web Form Config](../configuring/web-form-mode.md)**.

See **[Configuring Endpoints](../configuring/json-api-mode.md)** for details on setting
up each mode.

![Endpoints list](../assets/screenshots/endpoints-list.png#only-light)
![Endpoints list](../assets/screenshots/endpoints-list-dark.png#only-dark)

## Availability

An Endpoint returns HTTP 404 until the underlying **[Data Source](data-sources.md)** has finished compiling.
The Endpoints list shows a deployed status for each Endpoint, so you can check
readiness directly without navigating to the Data Source.
