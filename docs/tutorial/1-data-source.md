# 1. Upload a Data Source

A **[Data Source](../concepts/data-sources.md)** is the Excel file that powers your RuleX model.
In this step you will download the savings growth spreadsheet and upload it.

## Download the spreadsheet

[Download savings-calculator.xlsx](../assets/downloads/savings-calculator.xlsx){ .md-button }

The workbook has three input cells (`principal`, `annual_rate`, `years`) and two formula
cells (`final_amount`, `interest_earned`). Each cell has a defined name to keep the
formulas readable.

The input cells contain plain values, no formulas. RuleX writes the request inputs into
them before evaluating the model. Only static (non-formula) cells can be used as inputs.

## Upload to RuleX

1. Go to **Data Sources** in RuleX Admin.
2. Click **Add Data Source** in the top right corner.
3. Click **Upload an Excel file** and select `savings-calculator.xlsx`.
4. Set the name to `Savings Calculator`.
5. Leave the timezone on the default. This model does not use date values.
6. Click **Save**.

<video controls width="100%">
  <source src="../assets/videos/add-data-source-tutorial.webm" type="video/webm">
</video>

RuleX starts compiling your model immediately. The status in the Data Sources list
will show **PENDING** or **IN PROGRESS** while compilation runs.

Once the status changes to **Completed**, the model is ready. This usually takes
under a minute.
