# 9. Return a Scenario Comparison

So far every output has been a single value or a one-dimensional list. RuleX also
supports a **Spill Range** output that spans multiple rows and columns, a 2D
array whose size adjusts to the inputs.

This step adds an endpoint that returns a year-by-year growth table across three rate
scenarios: one percentage point below the rate you pass, the rate itself, and one
percentage point above. The number of rows grows with `years`, but the number of
columns is always three. Alongside it, a fixed 3-element range returns milestone
projections at 5, 10, and 20 years regardless of what `years` is.

## Download the workbook

[Download savings-scenarios.xlsx](../assets/downloads/savings-scenarios.xlsx){ .md-button }

The workbook has three input cells (`principal`, `annual_rate`, `years`), two scalar
outputs (`final_amount`, `interest_earned`), one 2D spill range anchored at `D3`
(`growth_scenarios`), and a fixed 3-cell range `B10` to `B12`.

## Upload as a Data Source

1. Go to **Data Sources** in RuleX Admin and click **Add Data Source**.
2. Upload `savings-scenarios.xlsx` and name it `Savings Scenarios`.
3. Click **Save** and wait for the status to reach **Completed**.

## Create the Schema

1. Click **Create New Schema** from the Data Source page.
2. Set the name to `Savings Scenarios`.

### Add inputs

| Name | Value Type | Sheet Name | Cell Reference | Optional |
| --- | --- | --- | --- | --- |
| principal | Integer | calculator | B2 | Unchecked |
| annual_rate | Decimal | calculator | B3 | Unchecked |
| years | Integer | calculator | B4 | Unchecked |

## Add outputs

Cell Outputs:

| Reference Type | Name | Value Type | Sheet Name | Cell Reference |
| --- | --- | --- | --- | --- |
| Cell | final_amount | Decimal | calculator | B7 |
| Cell | interest_earned | Decimal | calculator | B8 |

Range Outputs:

| Reference Type | Name | Sheet Name | Start Cell | End Cell |
| --- | --- | --- | --- | --- |
| Range | growth_scenarios | calculator | D3 | D3 |
| Range | milestones | calculator | B10 | B12 |

If the reference type is a range and start cell is same as end cell,
RuleX will try to treat it as a spill range.

For `growth_scenarios`, RuleX reads however many rows and columns have spilled at runtime.
With `years=3` it reads a 3×3 array; with `years=10` it reads a 10×3 array.
The three columns are always conservative (annual_rate − 0.01), base (annual_rate), and optimistic (annual_rate + 0.01).

The `milestones` values are the projected final balance at 5, 10, and 20 years at the base rate.

Click **Save and continue editing**.

## Create the Endpoint

1. Click **Add New Endpoint** from the Schema page.
2. Set the path to `/savings/scenarios`.
3. Set the mode to **JSON API** and the API Config to **Default**.
4. Click **Save**.

## See it in action

```http
POST https://<your-domain>/savings/scenarios
X-API-Key: <api-key>
Content-Type: application/json

{
  "principal": 10000,
  "annual_rate": 0.05,
  "years": 3
}
```

Response:

```json
{
  "final_amount": 11576.25,
  "interest_earned": 1576.25,
  "growth_scenarios": [
    [10400.00, 10500.00, 10600.00],
    [10816.00, 11025.00, 11236.00],
    [11248.64, 11576.25, 11910.16]
  ],
  "milestones": [
    [12762.82],
    [16288.95],
    [26532.98]
  ]
}
```

`growth_scenarios` is a 2D array: each row is a year, each column is a rate scenario.
Change `years` to 10 and the array grows to 10 rows; the three columns remain unchanged.

`milestones` is a column range in the spreadsheet (`B10:B12`), but the response shows
it as a 2D array with each value in its own row: `[[12762.82], [16288.95], [26532.98]]`.
RuleX always returns range values as a row-major 2D array, so a 3-row, 1-column range
becomes a 3×1 array rather than a flat list.

!!! tip "Extending scenarios requires no schema change"
    Because `growth_scenarios` is a Spill Range, RuleX reads whatever the formula
    produces at runtime. If you update the workbook formula to include more rate
    scenarios (say five columns instead of three), upload it as a new Data Source,
    point the Schema to it, and the endpoint immediately returns a wider array. No
    change to the Schema or Endpoint configuration is needed.
