# Contribute to Documentation

We use [Sphinx] to build the documentation. Historically, this has used
[reStructuredText] `.rst` as the syntax. You may see some pages written in
[Markdown] `.md` if the `myst-parser` dependency has been added to
the project. Docstrings in code must always use rST.

[Sphinx]: https://sphinx-doc.org
[reStructuredText]: https://docutils.sourceforge.io/rst.html
[Markdown]: https://commonmark.org

## Work on the `stable` Branch

**If you are fixing or improving existing docs, or writing about existing
features, you want to branch off of the `stable` branch, as well as target the
`stable` branch in the PR.**

If you use GitHub's UI to quickly edit a file, remember to select the `stable`
branch from the dropdown first. Otherwise, you'll end up submitting the fix
against `main`, and a maintainer will have to do extra work to retarget it.

Changes to `stable` docs will show up within minutes of being merged. Changes to
`main` will be unavailable until the next feature release. You'll rarely want to
work off of `main` for docs, unless you're working on docs for a new unreleased
feature.

## Building Docs

To build the docs locally, run `tox r -e docs`. To serve the docs locally, run
`python -m http.server -d docs/_build/dirhtml`. Then go to <https://localhost:8000>
in your browser to view the docs.

Documentation is hosted by Read the Docs. It is deployed on every change to the
`stable` branch. Each PR also generates a test build, which can be viewed by
clicking the "readthedocs" build check in the PR.

## Writing Docs

Writing about how to write documentation is surprisingly hard! We generally like
the ideas presented in [Diátaxis], which is a way of thinking about and doing
documentation.

[Diátaxis]: https://diataxis.fr

It can be very hard to assess whether a change is _better_ rather than only
_different_. Keep this in mind when deciding if you want to change something. If
a sentence is clear and understandable, even if you would say it differently,
then it should probably be left as-is.

The most common type of docs contribution is a typo fix. Check if the typo
happened in multiple places, and fix it everywhere. Don't submit typo fixes to
code comments that aren't visible in the deployed docs, unless you're also
working on that code. If you find multiple different typos, you can fix them in
separate commits to one PR, rather than multiple PRs. Make sure the typo is
really a typo, and not a correct sentence with a different meaning.

The libraries' docs have been written by many people over more than a decade.
This has introduced inconsistencies in style, focus, and technical level across
different parts of documentation over time. We recognize that there are many
ways in which documentation can be rewritten and improved. However, avoid huge
rewrites unless you have already checked with maintainers. If you're changing
more than a few sentences of text, and haven't received prior approval, you're
probably doing too much at once. It is very hard to review such changes,
especially from unknown users who we have not established trust with.

### Style, Spelling, and Grammar

Avoid referring to "you" or "we" outside of tutorials. State things directly;
"to do X, use Y" rather than "if you want to do X, then you should use Y."

Avoid phrases that might imply something is implicitly easy, such as "just do X"
or "the reason is obviously Y". Users are coming to the docs because something
wasn't obvious or easy for them at that moment.

The documentation is in English. If you are not a native English speaker, that's
OK, learners often catch issues that native speakers overlook. However, if a
maintainer would have to alter a significant portion of your PR, that's not a
great use of time. We also have a translation project, explained in the next
section.

Prefer [American spelling]. Use the [serial comma]; ("a, b, and c" rather than
"a, b and c"). That said, do not create a PR that tries to make everything
consistent, it's ok that existing docs use alternate spellings.

[American spelling]: https://www.oxfordinternationalenglish.com/differences-in-british-and-american-spelling/
[serial comma]: https://www.grammarly.com/blog/punctuation-capitalization/what-is-the-oxford-comma/

## Translating Docs

Currently, the community is working on translating Flask's documentation. We may
add other projects in the future.

You can find the translation project and instructions on how to contribute here:
<https://github.com/pallets-eco/flask-docs-translations>. We use [Weblate] to
manage translations. You'll need an account there. Then you can use the UI to navigate
to a language and find strings to translate.

[Weblate]: https://weblate.org
