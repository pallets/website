~~~~toml
name = "Flask"
logo = "flask-name.png"
~~~~

Flask is a lightweight [WSGI] web application framework. It is designed to make
getting started quick and easy, with the ability to scale up to complex
applications. It began as a simple wrapper around [Werkzeug] and [Jinja] and has
become one of the most popular Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project
layout. It is up to the developer to choose the tools and libraries they want to
use. There are many extensions provided by the community that make adding new
functionality easy.

[WSGI]: https://peps.python.org/pep-3333/
[Werkzeug]: werkzeug.md
[Jinja]: jinja.md

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello, World!"
```

```
$ flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
