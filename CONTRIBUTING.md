# Contributing to open-memory

Thanks for your interest in contributing! This project aims to keep memory simple: a single text/markdown file plus powerful regex search.

## Getting started

- Python 3.12+
- Install dependencies:
  - Core: none required
  - Dev: `uv add --dev pytest`
- Run a quick check (programmatic):
  - `uv run python -c "import re; from open_memory import TextMemory; m=TextMemory('An error occurred'); print([x.text for x in m.search_matches('error', flags=re.IGNORECASE)])"`

## Development workflow

1. Create a feature branch.
2. Make focused changes with clear commit messages.
3. Add tests under `tests/` when relevant.
4. Ensure lints/tests pass locally.
5. Open a PR with a concise description.

## Code style

- Prefer clear, readable code over cleverness.
- Keep functions small with single responsibilities.
- Avoid unnecessary abstractions; keep the memory model simple.

## Tests

- Use `pytest` for unit tests.
- Keep tests fast and independent.

## Documentation

- Keep `README.md` concise and high-signal.
- Update the diagram in `diagrams/` if behavior changes.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
