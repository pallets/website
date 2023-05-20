# Development Environment

Every project uses the same project layout and tools. It is helpful to be aware
of them and their documentation when contributing.

## Requirements Files

Each development environment uses a requirements file and the [pip-tools][] and
[pip-compile-multi][] tools to pin versions. This ensures that tests and builds
are reproducible when setting up a new environment or looking at previous tags.

The `requirements` folder contains `.in` files that list the direct, unpinned
requirements for each environment. pip-compile-multi uses the `.in` files to
generate `.txt` files that pin the entire dependency tree.

We do not use Dependabot to update these files as it is too noisy.

[pip-tools]: https://pip-tools.readthedocs.io
[pip-compile-multi]: https://pip-compile-multi.readthedocs.io

## Tests

[pytest][] is used to run the tests, found in the `tests` folder.

[tox][] is used to run different test environments, including Python versions,
style checks, documentation, and typing. The `tox.ini` file configures this.

We do not currently run [coverage][]. While our test suite is fairly robust,
we don't have consistent enough coverage to make the reports useful at this
time. We found that it does not impact our release quality.

[mypy][] is used for static type checking. Other tools may not give the same
results.

See [here](tests.md) for information about writing, running, and improving
tests and test coverage.

[pytest]: https://docs.pytest.org
[tox]: https://tox.wiki
[coverage]: https://coverage.readthedocs.io
[mypy]: https://mypy.readthedocs.io

## Documentation

[Sphinx][] is used to build the documentation. The `docs` folder contains `.rst`
files, which are [ReStructuredText][].

[Pallets-Sphinx-Themes][] contains the designs and extensions the projects use.

The docs are built and hosted on [Read the Docs][]. It will also check that the
docs build for pull requests.

See [here](docs.md) for information about writing and building documentation.

[Sphinx]: https://www.sphinx-doc.org
[Pallets-Sphinx-Themes]: https://github.com/pallets/pallets-sphinx-themes
[Read the Docs]: https://readthedocs.org

## Code Style

Code style tools are run automatically on each commit using [pre-commit][].
The `.pre-commit-config.yaml` file pins the versions of each tool.
[pre-commit.ci][] runs these checks and commits fixes automatically on pull
requests. It will also make PRs to update the pinned versions each month.

See [setup](setup.md) for how to enable pre-commit.

[black][] enforces code formatting.

[flake8][] enforces style "lint" rules. [flake8-bugbear][] catches more
opinionated rules.

[pyupgrade][] enforces using modern syntax for the Python versions we support.

[reorder_python_imports][] enforces a standard format and order for all imports
at the top of files.

[pre-commit]: https://pre-commit.com
[pre-commit.ci]: https://pre-commit.ci
[black]: https://black.readthedocs.io
[flake8]: https://flake8.pycqa.org
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[pyupgrade]: https://github.com/asottile/pyupgrade
[reorder_python_imports]: https://github.com/asottile/reorder-python-imports
