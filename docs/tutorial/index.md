# Tutorial: Savings Growth Calculator

In this tutorial, you are a financial services company setting up a savings growth
calculator in RuleX. By the end, you will have the same Excel model powering two
different consumer experiences: a JSON API your bank partners can integrate into their
own products, and a web form your customers can use directly in the browser.

## What you will build

A calculator that projects the final value and total interest earned on a savings
deposit at a fixed annual rate. It takes three inputs:

| Input | Description |
|---|---|
| `principal` | The initial deposit amount |
| `annual_rate` | The annual interest rate as a decimal (e.g. `0.05` for 5%) |
| `years` | The investment period in years |

And returns two outputs:

| Output | Description |
|---|---|
| `final_amount` | The value of the deposit at the end of the term |
| `interest_earned` | The total interest earned over the term |

## Steps

1. **[Upload a Data Source](1-data-source.md)**: upload the Excel model to RuleX
2. **[Define a Schema](2-schema.md)**: declare which cells are inputs and which are outputs
3. **[Create an Endpoint](3-endpoint.md)**: give the model a URL your bank partners can call
4. **[Call via the JSON API](4-json-api.md)**: see how bank partners integrate the API
5. **[Add Data Validations](5-validations.md)**: reject invalid inputs before they reach the model
6. **[Add Fixed Inputs](6-fixed-inputs.md)**: create a partner-specific endpoint with a promotional rate locked in
7. **[Publish a Web Form](7-web-form.md)**: give customers a browser interface, no code required
8. **[Write Tests](8-tests.md)**: validate the model against known inputs before deploying
9. **[Return a Scenario Comparison](9-ranges.md)**: return dynamic arrays using range and spill range output types

## Before you start

You will need a RuleX account. Sign up at [demo.rulex.coverstack.in](https://demo.rulex.coverstack.in) for free
if you do not have one.

Throughout this tutorial, API examples use `https://<your-domain>` as the base URL.
Replace it with the address of your RuleX api domain URL:

| Setup | Base URL |
|---|---|
| Full hosted access | `https://<your-domain>` |
| [Self-hosted exported server](../self-hosting/running-the-server.md) | `http://localhost:8000` |
