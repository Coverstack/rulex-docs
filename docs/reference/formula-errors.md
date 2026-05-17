# Formula Errors

When an output cell contains a formula error, RuleX returns the error string in the
response. The request does not fail.

This matches how Excel behaves: the cell shows the error string rather than a value,
and RuleX passes that string through unchanged.

## Error values

| Error | Meaning |
|---|---|
| `#NULL!` | Incorrect range operator or intersection of two ranges that do not intersect |
| `#DIV/0!` | Division by zero |
| `#VALUE!` | Wrong type of argument or operand |
| `#REF!` | Invalid cell reference |
| `#NAME?` | Unrecognised formula name |
| `#NUM!` | Invalid numeric value |
| `#N/A` | Value not available |
| `#CyclicRef` | Circular reference detected |

## Handling errors in your integration

Check output values for these strings in your integration code. For example:

```python
result = response.json()
if result["total"] in ("#VALUE!", "#N/A", "#DIV/0!", "#REF!",
                        "#NAME?", "#NUM!", "#NULL!", "#CyclicRef"):
    # handle the error
    ...
```

For the web form, error values are displayed as plain text in the results section.
