# Getting Started

RuleX turns Excel models into APIs. You upload your spreadsheet, configure which cells
are inputs and which are outputs, and get a URL that any application can call.

The business logic stays in Excel. If the spreadsheet gives the right answer, the API
gives the right answer.

![RuleX Admin dashboard](assets/screenshots/dashboard.png#only-light)
![RuleX Admin dashboard](assets/screenshots/dashboard-dark.png#only-dark)

## How it works

Setting up an API takes three steps:

1. Upload your Excel file as a **[Data Source](concepts/data-sources.md)**.
2. Define an **[Endpoint Schema](concepts/endpoint-schemas.md)**: map request fields to input cells and response
   fields to output cells.
3. Create an **[Endpoint](concepts/endpoints.md)**: assign a URL path, attach an API key, and the API is live.

The Endpoint URL works as a JSON API, a browser-accessible web form, or both.

## Try it for free

Visit [demo.rulex.coverstack.in](https://demo.rulex.coverstack.in/) to create a free
account.
The demo lets you upload Excel files, configure Schemas and Endpoints, and export
Endpoints for self-hosting.

There is **no limit** on the number of Excel files, Endpoints, or team members.

Some features require full hosted access. See
[Full Access Features](full-access-features.md) for details, or contact
[support@coverstack.in](mailto:support@coverstack.in) to get started.
