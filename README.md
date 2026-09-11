# Calculator CLI

Deterministic Python calculator CLI.

## Usage

```bash
calc add 1 2      # 3
calc sub 5 3      # 2
calc mul 4 6      # 24
calc div 8 2      # 4
calc add 1 2 --json  # {"result": 3}
```

## Error handling

- `calc div 1 0` → error, non-zero exit, division by zero
- `calc add foo 2` → error, invalid numeric input

## Testing

Tests via `pytest` through `aota.invoke test.run`:

```bash
pytest tests/test_calculator_core.py tests/test_cli.py -v
```

## Implementation

- `src/calculator/core.py` — add/sub/mul/div with division-by-zero
- `src/calculator/cli.py` — argparse CLI with --json
- `calc` — executable wrapper
