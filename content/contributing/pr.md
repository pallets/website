# Creating a Pull Request

If there is not an open issue for what you want to submit, prefer
opening one for discussion before working on a PR. You can work on any
issue that doesn't have an open PR linked to it or a maintainer assigned
to it. These show up in the sidebar. No need to ask if you can work on
an issue that interests you.

Include the following in your patch:

- Use `Black`_ to format your code. This and other tools will run automatically
  if you install `pre-commit`_ using the instructions below.
- Include tests if your patch adds or changes code. Make sure the test fails
  without your patch.
- Update any relevant docs pages and docstrings. Docs pages and docstrings
  should be wrapped at 80 characters.
- Add an entry in `CHANGES.rst`. Use the same style as other entries. Also
  include `.. versionchanged::` inline changelogs in relevant docstrings.

.. _Black: https://black.readthedocs.io
.. _pre-commit: https://pre-commit.com

## Start coding

Create a branch to identify the issue you would like to work on. If you're
submitting a bug or documentation fix, branch off of the latest `A.B.x` branch.

```
$ git fetch origin
$ git checkout -b your-branch-name origin/2.0.x
```

If you're submitting a feature addition or change, branch off of the "main" branch.

```
$ git fetch origin
$ git checkout -b your-branch-name origin/main
```

Using your favorite editor, make your changes, [committing as you go][].

If you are in a codespace, you will be prompted to [create a fork][] the first
time you make a commit. Enter `Y` to continue.

Include tests that cover any code changes you make. Make sure the test fails
without your patch. Run the tests as described below.

Push your commits to your fork on GitHub and [create a pull request][]. Link to the
issue being addressed with `fixes #123` in the pull request description.

```
$ git push --set-upstream origin your-branch-name
```

[committing as you go]: https://afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
[create a fork]: https://docs.github.com/en/codespaces/developing-in-codespaces/using-source-control-in-your-codespace#about-automatic-forking
[create a pull request]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
