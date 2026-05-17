# Excel Compatibility

RuleX follows **Excel 2021** behaviour as the baseline for all formula evaluation.
This includes dynamic array behaviour: formulas that produce multiple results spill
into adjacent cells automatically. You do not need to use Ctrl+Shift+Enter (CSE) to
enter array formulas.

## Google Sheets

If your model was built in Google Sheets, two areas are likely to behave differently.

### Dynamic arrays and ARRAYFORMULA

Google Sheets does not default to dynamic arrays. To produce multi-cell results in
Google Sheets, you wrap formulas in `ARRAYFORMULA`. RuleX does not support
`ARRAYFORMULA`, which is a Google Sheets-specific function.

If your model uses `ARRAYFORMULA`, rewrite those formulas using native Excel dynamic
array behaviour before uploading. In most cases this means removing the `ARRAYFORMULA`
wrapper. The formula will spill automatically in RuleX.

### FILTER syntax

Excel and Google Sheets use different syntax for `FILTER`.

Excel:
```
=FILTER(array, include, [if_empty])
```

Google Sheets:
```
=FILTER(range, condition1, [condition2, ...])
```

These are not compatible. If your model uses `FILTER` with Google Sheets syntax,
rewrite it using the Excel syntax before uploading.

## LibreOffice

LibreOffice only supports CSE-based array formulas (entered with
Ctrl+Shift+Enter). It does not support dynamic arrays or automatic spilling.

If your model was built in LibreOffice and uses CSE array formulas, test carefully
after uploading to RuleX. The formula logic should still work, but the spilling
behaviour will follow Excel 2021 rules, not LibreOffice rules.

## General guidance

If your model was built in Google Sheets or LibreOffice, verify each formula
against Excel 2021 behaviour before using the Endpoint in production. The
**[Supported Formulas](supported-formulas.md)** list shows which functions RuleX
implements.
