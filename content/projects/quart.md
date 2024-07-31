~~~~toml
name = "Quart"
logo = "quart-name.png"
~~~~

Quart is a fast [ASGI] web application framework. It is the async version of
[Flask], providing the same developer API and a similar extension ecosystem.
It also provides additional ASGI features such as handling WebSocket routes and
better concurrent streaming request/response performance.

[ASGI]: https://asgi.readthedocs.io
[Flask]: flask.md

```python
# hello.py
from quart import Quart

app = Quart(__name__)

@app.route('/')
async def greet():
    return 'Hello, World!'
```

```
$ export QUART_APP=hello:app
$ quart run
```
