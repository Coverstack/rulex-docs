# Type Casting

RuleX converts values between JSON types and Excel types automatically.

## Inputs (JSON to Excel)

| Schema type | Expected JSON format | Excel type |
|---|---|---|
| Text | String | Text |
| Integer | Integer | Number |
| Decimal | Number (integer or decimal) | Number |
| Boolean | `true` or `false` | Boolean |
| Date | ISO 8601 date string, e.g. `"2024-06-15"` | Date serial |
| Date & Time | ISO 8601 datetime string, e.g. `"2024-06-15T09:30:00"` | Datetime serial |

Date and datetime values are interpreted in the timezone configured on the **[Data Source](../concepts/data-sources.md)**. If your Data Source timezone is `Asia/Kolkata`, then `"2024-06-15T09:30:00"`
is treated as 9:30 AM IST.

## Outputs (Excel to JSON)

| Excel type | JSON format |
|---|---|
| Number (integer) | Integer |
| Number (decimal) | Float |
| Boolean | `true` or `false` |
| Text | String |
| Date | ISO 8601 date string, e.g. `"2024-06-15"` |
| Datetime | ISO 8601 datetime string, e.g. `"2024-06-15T09:30:00"` |
| Formula error | Error string, e.g. `"#VALUE!"` |
| Range | 2D JSON array, e.g. `[[1, 2], [3, 4]]` |

Date and datetime outputs are serialised in the Data Source timezone.

!!! note
    If the output is a range, values in the array are serialised as per the Excel output.
    One exception is for Date and Datetime types. They are serialised as numbers.
    `1` being Jan 1, 1900.

## Web form inputs

Web form fields enforce the correct input format for each type. Number fields only
accept numeric input, date fields show a date picker, and boolean fields use a
dropdown. The same type casting rules apply when the form is submitted.
