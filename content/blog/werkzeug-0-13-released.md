~~~~toml
title = "Werkzeug 0.13 Released"
author_name = "David Lord"
published = 2017-12-07
tags = ["releases"]
~~~~

The Pallets team is pleased to release [Werkzeug](https://werkzeug.palletsprojects.com)
0.13. Changes include:

* **Deprecated Python 2.6 and 3.3 support.** The next version, 0.14, will remove
  support.
* The built-in development server supports receiving requests
  with `Transfer-Encoding: chunked`.
* Header options without an extended encoding can contain single quotes. For
  example, `filename=t'es't.txt` is now valid.
* Removed `werkzeug.script` in favor of [Click](https://click.palletsprojects.com).

[Read the full changelog.](https://werkzeug.palletsprojects.com/page/changes/#version-0-13)

### Install or upgrade

Install from [PyPI](https://pypi.org/project/Werkzeug/0.13/) with pip:

```
pip install -U Werkzeug
```

The PGP key ID used for this release
is [David Lord: 43368a7aa8cc5926](https://keybase.io/davidism).

### Get Involved

Werkzeug and the Pallets team depends on you, the community. Whether you report issues,
write documentation, create patches, or answer questions, we appreciate all the help you
provide. We updated
the [contributing guide](https://github.com/pallets/werkzeug/blob/master/CONTRIBUTING.rst)
to help make it easier to get started.
