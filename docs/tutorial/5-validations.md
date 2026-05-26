# 5. Add Data Validations

RuleX enforces Excel Data Validation rules automatically. Once you add rules to your
spreadsheet cells, RuleX checks every incoming request against them with no extra
configuration needed. Invalid inputs are rejected before the model runs, so
bank partners get fast, specific errors instead of bad results.

## Download the updated workbook

[Download savings-calculator-v2.xlsx](../assets/downloads/savings-calculator-v2.xlsx){ .md-button }

This workbook has the following validation rules already applied to the
input cells:

| Cell | Rule | Error message |
|---|---|---|
| `principal` | Decimal ≥ 1000 | Principal must be at least 1000 |
| `annual_rate` | Decimal between 0.01 and 1 | Annual rate must be between 0.01 and 1 |
| `years` | Whole number between 1 and 30 | Term must be between 1 and 30 years |

## Upload as a new Data Source

**[Data Sources](../concepts/data-sources.md)** are immutable. To use the updated model, upload it as a new Source.

1. Go to **Data Sources** in RuleX Admin and click **Add Data Source**.
2. Upload `savings-calculator-v2.xlsx` and name it `Savings Calculator v2`.
3. Click **Save** and wait for the status to reach **Completed**.

## Update the Schema

1. Go to **Endpoint Schemas** in RuleX Admin and open `Savings Projection`.
2. Click the search icon under **Source**, select `Savings Calculator v2`.
3. Click **Save**.

All endpoints backed by this Schema now use the updated model. The validation rules
are active immediately.

## See it in action

Send a request with a principal below the minimum:

```http
POST https://<your-domain>/savings/projection
X-API-Key: <api-key>
Content-Type: application/json

{
  "principal": 500,
  "annual_rate": 0.05,
  "years": 10
}
```

RuleX rejects the request with HTTP 422 before the model runs:

```json
{
  "detail": [
    {
      "type": "invalid_data",
      "loc": [
        "principal"
      ],
      "msg": "Value must be greater than or equal to 1000",
      "input": 500
    }
  ]
}
```

In the web form you will publish in step 7, the same error appears inline next to the field as the customer types.
