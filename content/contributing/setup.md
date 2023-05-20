# Development Environment Setup

## GitHub Codespaces

`GitHub Codespaces`_ creates a development environment that is already set up for the
project. By default it opens in Visual Studio Code for the Web, but this can
be changed in your GitHub profile settings to use Visual Studio Code or JetBrains
PyCharm on your local computer.

-   Make sure you have a `GitHub account`_.
-   From the project's repository page, click the green "Code" button and then "Create
    codespace on main".
-   The codespace will be set up, then Visual Studio Code will open. However, you'll
    need to wait a bit longer for the Python extension to be installed. You'll know it's
    ready when the terminal at the bottom shows that the virtualenv was activated.
-   Check out a branch and `start coding`_.

.. _GitHub Codespaces: https://docs.github.com/en/codespaces
.. _devcontainer: https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers

## Local Environment

-   Make sure you have a `GitHub account`_.
-   Download and install the `latest version of git`_.
-   Configure git with your `username`_ and `email`_.

    .. code-block:: text

        $ git config --global user.name 'your name'
        $ git config --global user.email 'your email'

-   Fork Flask to your GitHub account by clicking the `Fork`_ button.
-   `Clone`_ your fork locally, replacing ``your-username`` in the command below with
    your actual username.

    .. code-block:: text

        $ git clone https://github.com/your-username/flask
        $ cd flask

-   Create a virtualenv. Use the latest version of Python.

    - Linux/macOS

      .. code-block:: text

         $ python3 -m venv .venv
         $ . .venv/bin/activate

    - Windows

      .. code-block:: text

         > py -3 -m venv .venv
         > .venv\Scripts\activate

-   Install the development dependencies, then install Flask in editable mode.

    .. code-block:: text

        $ python -m pip install -U pip setuptools wheel
        $ pip install -r requirements/dev.txt && pip install -e .

-   Install the pre-commit hooks.

    .. code-block:: text

        $ pre-commit install --install-hooks

.. _GitHub account: https://github.com/join
.. _latest version of git: https://git-scm.com/downloads
.. _username: https://docs.github.com/en/github/using-git/setting-your-username-in-git
.. _email: https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address
.. _Fork: https://github.com/pallets/flask/fork
.. _Clone: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork
