from itertools import batched
from pathlib import Path

import yaml


def define_env(env):
    _data_path = Path(__file__).parent / "docs" / "data" / "formulas.yaml"
    with _data_path.open() as f:
        formulas = env.variables["formulas"] = sorted(yaml.safe_load(f))

    @env.macro
    def formulas_table(cols=5):
        header = "| List of formulas |" + " |" * (cols - 1)
        separator = "|" + "---|" * cols
        rows = [
            "| " + " | ".join((*chunk, *(("",) * (cols - len(chunk))))) + " |"
            for chunk in batched(formulas, cols)
        ]
        return "\n".join((header, separator, *rows))
