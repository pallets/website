# Development Environment Setup

## GitHub Codespaces

[GitHub Codespaces][] creates a development environment that is already set up
for the project. By default it opens in Visual Studio Code for the Web, but this
can be changed in your GitHub profile settings to use Visual Studio Code or
JetBrains PyCharm on your local computer.

-   Make sure you have a [GitHub account][].
-   From the project's repository page, click the green "Code" button and then
    "Create codespace on main".
-   The codespace will be set up, then Visual Studio Code will open. However,
    you'll need to wait a bit longer for the Python extension to be installed.
    You'll know it's ready when the terminal at the bottom shows that the
    virtualenv was activated.
-   Check out a new branch and start coding.

## Local Environment

-   Make sure you have a [GitHub account][].
-   Download and install the [latest version of git][].
-   Configure git with your [username][] and [email][]. GitHub provides everyone
    a placeholder email if you don't want to publish yours.
    ```
    $ git config --global user.name 'your name'
    $ git config --global user.email 'your email'
    ```
-   [Fork][] the project to your GitHub account by clicking the "Fork" button.
-   Clone your fork locally, replacing `your-username` and `project` in the
    command below with your actual username and the actual project name.
    ```
    $ git clone https://github.com/your-username/project
    $ cd project
    ```
-   Create a virtualenv. Use the latest version of Python.
    -   Linux/macOS
        ```
        $ python3 -m venv .venv
        $ . .venv/bin/activate
        ```
    -   Windows
        ```
        > py -3 -m venv .venv
        > .venv\Scripts\activate
        ```
-   Install the development dependencies, then install Flask in editable mode.
    In the future, you can run this again to update the dependencies.
    ```
    $ pip install -r requirements/dev.txt && pip install -e .
    ```
-   Install the pre-commit hooks.
    ```
    $ pre-commit install --install-hooks
    ```

[GitHub Codespaces]: https://docs.github.com/en/codespaces
[GitHub account]: https://github.com/join
[latest version of git]: https://git-scm.com/downloads
[username]: https://docs.github.com/en/github/using-git/setting-your-username-in-git
[email]: https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address
[Fork]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
