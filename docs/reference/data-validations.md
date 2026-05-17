# Data Validations

RuleX enforces Excel Data Validation rules automatically. If your spreadsheet has
validation rules on input cells, those rules apply to every request without any
extra configuration.

## How it works

When a request comes in, RuleX feeds the inputs into the model and checks each input
cell's validation rule. If any input fails, the request is rejected before the
calculation runs.

For the JSON API, a failed validation returns HTTP 422 with field-level error details:

```json
{
  "detail": [
    {
      "loc": ["quantity"],
      "msg": "Value must be between 1 and 100"
    }
  ]
}
```

For the web form, errors appear inline next to the relevant field.

## Supported validation types

RuleX supports all of the following Excel Data Validation types:

- **Whole number:** must be an integer within a specified range
- **Decimal:** must be a number within a specified range
- **List:** must be one of a fixed set of values
- **Date:** must be a date within a specified range
- **Text length:** text must meet a length constraint
- **Custom:** must satisfy a custom formula

The error message shown to the consumer is the one you configured in the Excel
validation dialog. If no custom message is set, RuleX uses a generic message.

!!! note
    Only the Data Validation rules that reject user input are considered by RuleX.
    Rules that are informational or warning are silently ignored.
