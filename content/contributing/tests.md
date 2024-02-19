# Tests

## Run Tests

Run the test suite with pytest.

```
$ pytest
```

This runs the tests for the current environment, which is usually sufficient. CI
will run the full suite when you submit your pull request. You can run the full
test suite with tox if you don't want to wait.

```
$ tox
```

## Coverage

Generating a report of lines that do not have test coverage can indicate
where to start contributing. Run `pytest` using `coverage` and
generate a report.

If you are using GitHub Codespaces, `coverage` is already installed
so you can skip the installation command.

```
$ pip install coverage
$ coverage run -m pytest
$ coverage html
```

Open `htmlcov/index.html` in your browser to explore the report.

Read more about [coverage](https://coverage.readthedocs.io).
