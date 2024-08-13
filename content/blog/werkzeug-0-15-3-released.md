~~~~toml
title = "Werkzeug 0.15.3 Released"
author_name = "David Lord"
published = 2019-05-14
tags = ["releases", "security"]
~~~~

Werkzeug 0.15.3 has been released, followed closely by 0.15.4. Both fix
bugs and compatibility issues. The [changelog][] lists the changes in
detail, which include:

* The debugger pin is unique per Docker container.
* Fix issues with the arguments to the `Unauthorized` HTTP exception.
* Fix `ProfilerMiddleware` filenames, and get `LintMiddleware` working
  on Python 3.
* Bytes passed to URLs will be correctly decoded rather than having a
  `b` prefix.

[changelog]: https://werkzeug.palletsprojects.com/en/0.15.x/changes/#version-0-15-3


Debugger Pin Security
