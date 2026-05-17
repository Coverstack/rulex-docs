# API Config

An API Config holds the credentials for your JSON API **[Endpoints](../concepts/endpoints.md)**. You can assign one
API Config to multiple Endpoints, which means a single key can cover a group of
related Endpoints.

## Creating an API Config

Go to the **Endpoint** in RuleX Admin and click the plus button (+) in JSON API Configs section.
Give it a name, and save.

RuleX generates a 64-character API key automatically.
Click the eye button next to the API Config to view the API key.

![API Config detail page](../assets/screenshots/api-config-detail.png#only-light)
![API Config detail page](../assets/screenshots/api-config-detail-dark.png#only-dark)

## IP whitelist

The IP whitelist restricts which IP addresses can use the key. Leave it blank to
allow requests from any IP. Add individual IP addresses or CIDR ranges to restrict
access.
