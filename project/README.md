# project

Small example Python package used for demos and tests.

Contents
- `project.app` - simple in-memory customer store and demo CLI
- `project.models` - `Customer` dataclass and helpers
- `project.utils.logging_utils` - small logger helper

Quick start

1. From the package root run the demo:

```powershell
Set-Location 'C:\Companies Courses\GIT\my-python-app'
python -m project.app
```

2. Use the package interactively from the project root:

```powershell
Set-Location 'C:\Companies Courses\GIT\my-python-app'
python -c "from project import app; print([c.to_dict() for c in app.list_customers()])"
```

Development

- Install the test dependencies:

```powershell
Set-Location 'C:\Companies Courses\GIT\my-python-app'
pip install -r project/requirements.txt
```

- Run tests with `pytest` (tests will live under `project/tests`).

Contributing

This repo is intentionally small. Open a PR to add features or tests.
