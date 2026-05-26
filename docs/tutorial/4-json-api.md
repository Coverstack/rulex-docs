# 4. Call via the JSON API

Your bank partners integrate the Endpoint by sending HTTP requests from their application.
Here is what that looks like from their side.

## The request

A bank partner sends a `POST` request with the three Schema inputs in the body.

```http
POST https://<your-domain>/savings/projection
X-API-Key: <api-key>
Content-Type: application/json

{
  "principal": 10000,
  "annual_rate": 0.05,
  "years": 10
}
```

!!! note
    Replace `<your-domain>` with your RuleX api domain and `<api-key>`
    with the key from the API Config. For a [self-hosted exported server](../self-hosting/running-the-server.md),
    replace `https://<your-domain>` with `http://localhost:8000`.

The response contains the two outputs:

```json
{
  "final_amount": 16288.95,
  "interest_earned": 6288.95
}
```

The bank partner can make this request from any HTTP client or directly from their
application code.

## Try it in the Swagger UI

!!! info "Full access feature"
    Swagger UI requires full hosted access.
    [Learn more](../full-access-features.md)

Each JSON API Endpoint has a built-in Swagger UI where you can explore the request and
response schema and try calls directly from the browser.

1. Open the Endpoint in RuleX Admin.
2. Click **View API Docs**.

The Swagger UI opens with the full schema pre-populated.
Click **Authorize**, enter your API Key, click **Authorize** and then **close**.

Click **Try it out**, enter values, and click **Execute** to see a live response.

## Validation

RuleX validates every request before running the model:

- All required inputs must be present.
- Types must match. Sending a string for a `Decimal` field returns `400 Bad Request`.
- Excel Data Validation rules on the input cells are also enforced. You will add these in the next step.

Invalid requests are rejected before reaching the model.
