# Contributing to gorkestra

Thanks for wanting to contribute! Here's how:

## Getting Started

1. Fork the repo
2. Clone your fork
3. Install dev dependencies: `pip install -e ".[dev]"`
4. Create a branch: `git checkout -b feature/your-feature`

## Development

```bash
# Run tests
pytest

# Format code
black gorkestra/
ruff gorkestra/

# Type check
mypy gorkestra/
```

## Pull Requests

1. Update tests for new features
2. Update README if needed
3. Follow existing code style
4. Write clear commit messages

## Adding Personas

Want to add a new persona? 

1. Add it to `gorkestra/personas/builtin.py`
2. Add tests in `tests/test_personas.py`
3. Update README with the new persona

## Code of Conduct

Be cool. Don't be not cool.
