~~~~toml
title = "Werkzeug 0.15.5 Released"
author_name = "David Lord"
published = 2019-07-17
tags = ["releases", "security"]
~~~~

Werkzeug 0.15.5 has been released, containing bug and security fixes.
The [changelog][] lists the changes in detail, which include:

* `SharedDataMiddleware` safely handles drive names in paths on Windows.
* The reloader no longer causes an `Exec format error` in many common
  situations.
* The reloader works around an issue when using the pydev debugger.

[changelog]: https://werkzeug.palletsprojects.com/en/0.15.x/changes/#version-0-15-5


Security fix for `SharedDataMiddleware` on Windows
