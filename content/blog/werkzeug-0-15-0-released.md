~~~~toml
title = "Werkzeug 0.15.0 Released"
author_name = "David Lord"
published = 2019-03-19
tags = ["releases"]
~~~~

The Pallets team is pleased to release Werkzeug 0.15.0. This represents
over a year of work from the community and maintainers, and as such
there is an unusually long list of changes. Some of the notable ones
are listed below, but there are many more throughout the framework.
[Read the full changelog](https://werkzeug.palletsprojects.com/en/0.15.x/changes/)
to understand what changes may affect your code when upgrading.

* Building URLs is ~7x faster.
* Redirects now use HTTP code 308 by default. This preserves the method
  and form data.
* `int` and `float` URL converters can handle negative numbers.
* The debugger saw a number of improvements. Python 3's chained
  exceptions are correctly displayed and logged. Frames of user code
  are highlighted to make it easier to read tracebacks.
* The reloader is much better at detecting how to re-run itself. It
  handles `python -m` as well as non-Python executable scripts.
* The test client takes a `json` parameter, and the response class has
  a `get_json` method. This makes testing JSON APIs much more
  straightforward.
* URLs with Unicode or percent-escapes are handled better. Quoting when
  converting between URIs and IRIs is more consistent, and the unquoted
  URL is logged by the dev server rather than showing percent escapes.
* Deprecation warnings have been added throughout the code in
  preparation for version 1.0.
* Werkzeug now uses [pre-commit][], [black][], [reorder-python-imports][],
  and [flake8][] to provide consistent code formatting. The code also
  moved to a `src` directory layout.
* And much more!

[pre-commit]: https://pre-commit.com/
[black]: https://black.readthedocs.io/en/stable/
[reorder-python-imports]: https://github.com/asottile/reorder_python_imports
[flake8]: http://flake8.pycqa.org/en/latest/


`werkzeug.contrib` has been deprecated
