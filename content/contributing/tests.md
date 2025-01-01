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

Most projects do not actively check code coverage percentage. It can be checked
by running pytest with coverage.

```
$ coverage run -m pytest
$ coverage report
$ coverage html  # open htmlcov/index.html in your browser
```

This generates a report of lines that do not have test coverage. You can use
this to confirmcan indicate
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


## Writing


Add tests that demonstrate that your code works, and ensure all tests pass.
Tests are located in the `tests` directory. We use [pytest] as our test runner.
Run `pytest` to run all the tests with the current Python version.

[pytest]: https://pytest.org

Tests are generally organized by topic in `test_{topic}.py` files, and within
each file each test is a `test_{specific}` function. The test function name
should be unique, somewhat descriptive without being too long.

Each test should test one thing, using `assert` statements to check expected
properties of that one thing. If you have multiple test cases, use the
[`@pytest.mark.parametrize`][parametrize] decorator to run the same test with
different arguments.

[parametrize]: https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
