# Endpoint Schemas

An Endpoint Schema defines the inputs and outputs for a given **[Data Source](data-sources.md)**. The Schema
is what the API request and response are based on.

You can define multiple Schemas for a single **[Source](data-sources.md)**. This is useful when you need
different input/output combinations from the same Excel model.

![Schema editor](../assets/screenshots/schema-editor.png#only-light)
![Schema editor](../assets/screenshots/schema-editor-dark.png#only-dark)

## Inputs

Each input maps a named field to a static cell in the spreadsheet.

Select the sheet from the dropdown and enter the cell address (for example `B2`) in the **Cell Ref** input box.

**Supported types:**

| Type | Description |
|---|---|
| Text | Any text value |
| Integer | Whole number |
| Decimal | Decimal number |
| Boolean | TRUE or FALSE |
| Date | Calendar date |
| Date & Time | Date and time |

Each input can be marked **Required** or **Optional**. Optional inputs are not passed
to Excel as inputs if left empty in the request.

## Outputs

Each output maps a named field to a cell or range in the spreadsheet.

Select the sheet from the dropdown. For each output type:

- **Single cell:** returns a scalar value (number, text, boolean, date). Enter the cell address.
- **Range:** returns a 2D array. Enter the start cell and end cell.
- **Spill range:** set the start cell and end cell to the same cell.
  This cell is the anchor cell of the spill range.
  RuleX reads the full spill range of the dynamic array formula in that cell.

!!! note
    If the provided cell does not spill, then it is treated as 1×1 range. 

## Updating an Excel model

If you update your Excel file, upload it as a new **[Data Source](data-sources.md)** and edit the Schema to
point at the new Source. RuleX uses the updated formulas immediately. Your **[Endpoints](endpoints.md)**
do not need to change.

!!! note
    This only works if the existing Schema is still valid against the new Source.
    All sheet names referenced in inputs and outputs must exist in the new file,
    and all input cell references must still be static cells.

!!! danger "Warning"
    Wait for the new Source to finish compiling before switching the Schema to point at it.
    If an Endpoint is live and serving requests, pointing the Schema at an incomplete Source
    will cause the Endpoint to return HTTP 404 until compilation finishes.
