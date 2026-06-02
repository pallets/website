# Development Environment Setup

This is a detailed guide on how to set up Python, Git, and a development
environment for our projects. Following these instructions will ensure
that every contributor has the same tools installed at the same versions in the
same way, which makes it easier for everyone to help each other.

If you're already familiar with contributing to Python projects, you can refer
to the [Quick Reference](quick.md) instead.

[venv]: https://docs.python.org/3/library/venv.html
[pip]: https://pip.pypa.io

## GitHub and Git

- Make sure you have a [GitHub account][github].
-   Download and install the [latest version of Git][git].
-   Configure Git with your [name] and [email].
    ```
    $ git config --global user.name 'your name'
    $ git config --global user.email 'your email'
    ```
-   [Fork] the project to your GitHub account by clicking the "Fork" button.
    Un-check the box that says "Copy the main branch only", as you will
    also need the `stable` branch.
-   Clone your fork locally, replacing `your-username` and `project` in the
    command below with your actual username and the actual project name. Change
    directory into the cloned project.
    ```
    $ git clone https://github.com/your-username/project
    $ cd project
    ```

[github]: https://github.com
[git]: https://git-scm.com/downloads
[name]: https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git
[email]: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address
[Fork]: https://docs.github.com/en/get-started/quickstart/fork-a-repo

## Install Python

Install the latest version of Python.

-   Linux: `python3` is likely already installed, otherwise use your
    system's package manager to install it.
-   macOS/Windows: Download and run the appropriate installer from
    https://python.org/downloads/. The yellow "Download" button near the top
    left of the page will download the latest stable version.


## Install Python dependencies

Pallets projects use two different ways of managing dependencies: `pip` and `uv`.
Projects are being upgraded to use `uv`, but many projects still use `pip`.
If the project has `requirements` folder, that means it is using the older `pip` flow.
Check for that folder and follow the appropriate steps below.

### Projects with a `requirements` directory

-   Create and activate a virtualenv.
    -   Linux/macOS
        ```
        $ python3 -m venv .venv
        $ . .venv/bin/activate
        ```
        -   On Ubuntu or Debian, you'll need to install `venv` first, otherwise
            the above command will fail.
            ```
            $ sudo apt install python3-venv
            ```
    -   Windows
        ```
        > py -3 -m venv .venv
        > .venv\Scripts\activate
        ```
-   Install the development dependencies, then install the project in editable mode.
    In the future, you can run this again to update the dependencies.
    ```
    $ pip install -r requirements/dev.txt && pip install -e .
    ```
    -   On Windows CMD, `&&` doesn't work, so run the two commands separately.

### Projects without a `requirements` directory

[Install `uv`.][uv]

[uv]: https://docs.astral.sh/uv/getting-started/installation/

Install dev dependencies:

```
$ uv sync
```

Activate the virtualenv (Mac and Linux):

```
$ . .venv/bin/activate
```

Activate the virtualenv (Windows):

```
> .\.venv\Scripts\activate
```

Any time you open a new terminal, you need to activate the virtualenv again. If
you've pulled from upstream recently, you can re-run the `uv sync` command to
get the current dev dependencies.

## Install pre-commit hooks

Pre-commit hooks automatically run linters and formatters before each git commit, catching style issues early so they don't appear as CI failures later.

```
$ pre-commit install --install-hooks
```


## Debugger

Many IDEs, including [PyCharm] and [VS Code], include a debugger UI. There are also
standalone debuggers such as [pudb], [pdbp], [ipdb], and [bpdb].

[pudb]: https://github.com/inducer/pudb#readme
[pdbp]: https://github.com/mdmintz/pdbp#readme
[ipdb]: https://github.com/gotcha/ipdb#readme
[bpdb]: https://docs.bpython-interpreter.org/en/latest/bpdb.html
