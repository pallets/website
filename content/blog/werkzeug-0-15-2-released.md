~~~~toml
title = "Werkzeug 0.15.2 Released"
author_name = "David Lord"
published = 2019-04-02
tags = ["releases"]
~~~~

Werkzeug 0.15.2 has been released. The
[changelog](https://werkzeug.palletsprojects.com/page/changes/#version-0-15-2)
lists the changes in detail, which include:

* Fix an issue where code generation would cause coverage to fail.
* Fixed some issues with the new test client redirect code. If no
  cookies are stored, the cookie header is removed. Changes to the
  environ by the app don't affect the client.
* The "werkzeug" logger doesn't log messages twice if user code has
  already configured logging.

## Install or Upgrade

Install from [PyPI](https://pypi.org/project/Werkzeug/) with pip:

    pip install -U Werkzeug
