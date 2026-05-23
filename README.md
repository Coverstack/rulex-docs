# RuleX Docs

Documentation for [RuleX](https://coverstack.in/rulex/), published at [docs.rulex.coverstack.in](https://docs.rulex.coverstack.in).

Built with [Zensical](https://zensical.dev).

## Development

Requires [uv](https://docs.astral.sh/uv/).

Run the following command to start the web server

```bash
uv run zensical serve
```

## Adding a formula

Add the formula name in alphabetical order in `docs/data/formulas.yaml`. The count and table on the Supported Formulas page update automatically on the next build.

> **Note:** Quote entries that YAML would misparse — for example, `"TRUE"` and `"FALSE"`.

## Diagrams

Architecture diagrams are hand-drawn in [Excalidraw](https://excalidraw.com). Source files are maintained in `excalidraw/`.
Each diagram is exported as a light/dark SVG pair into `docs/assets/diagrams/`.

## Feedback

You can raise a new issue on github or use our [feedback form](https://forms.gle/UrHtUNHCrvW2yeM98) to help us improve the documentation.
