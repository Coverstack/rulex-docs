# Organisation

Every RuleX account belongs to an Organisation. When you sign up, you either create a
new Organisation or accept an invitation to join an existing one.

![Organisation onboarding](../assets/screenshots/organisation-onboarding.png#only-light)
![Organisation onboarding](../assets/screenshots/organisation-onboarding-dark.png#only-dark)

## Domain

Each Organisation gets a domain assigned at creation time. This domain is the base URL
for all your Endpoints. If your domain is `example.rulex.coverstack.in`, an **[Endpoint](endpoints.md)** at
path `/calculate/price` is reachable at
`https://example.rulex.coverstack.in/calculate/price`.

You can view your domain in **Organisation > Settings** in RuleX Admin.

![Organisation settings](../assets/screenshots/organisation-settings.png#only-light)
![Organisation settings](../assets/screenshots/organisation-settings-dark.png#only-dark)

## Data isolation

All data in RuleX (**[Data Sources](data-sources.md)**, **[Schemas](endpoint-schemas.md)**, **[Endpoints](endpoints.md)**, **[Team members](../team-management.md)**) belongs to your
Organisation and is completely isolated from other Organisations.
