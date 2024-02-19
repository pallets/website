# Contribute to Documentation

We use [Sphinx][] and [ReStructuredText][] to write the documentation.

To build the docs locally, run `tox r -e docs`. To serve the docs locally, run
`python -m http.server docs/_build/dirhtml`. Then go to <https://localhost:8000>
in your browser to view the docs.

Documentation is hosted by Read the Docs. They are built and deployed for any
changes to the `main` and `A.B.x` feature branches. Each PR also generates a
test build.

[Sphinx]: https://sphinx-doc.org
[reStructuredText]: https://docutils.sourceforge.io/rst.html
