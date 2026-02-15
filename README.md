[![tests](https://github.com/cruz-torres-dev/python-debugging-lab/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/cruz-torres-dev/python-debugging-lab/actions/workflows/tests.yml)

# python-debugging-lab

Small, real-world Python bugfix cases (buggy vs fixed) with tests and Docker. Focused on debugging via logs/traces and runtime behavior.

## Project structure

- `src/buggy/`: intentionally buggy implementations
- `src/fixed/`: corrected implementations
- `tests/`: regression tests (pytest)
- `logs/`: sample logs / stack traces
- `docker/`: Dockerfile + docker-compose

## Run locally

```bash
pip install -r requirements.txt
python -m pytest -q
