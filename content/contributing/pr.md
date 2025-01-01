# Creating a Pull Request

If there is not an open issue for what you want to work on, prefer opening one
for discussion before working on a PR. See how to [Report an Issue](issues.md)
or [Request a Feature](features.md).

Anyone is welcome to work on any open issue without asking first. Check that the
issue is not marked as assigned (in the sidebar) and is not already linked to an
open PR. Do not ask to be assigned to an issue. Maintainers only use assignment
for themselves or during live sprints to avoid conflicting work.

Check [Environment Setup](setup.md) or [Quick Reference](quick.md) for how to
set up your development environment and run tests. This guide assumes you've
done that and used the GitHub CLI to fork and clone the repository and add the
upstream remote.

## Create a Branch

To work on a bug or documentation fix, switch to the `stable` branch (if the
project has it), otherwise switch to the `main` branch. To update this target
branch, pull from `upstream`. Create a work branch with a short descriptive
name. The branch name does not need to include the issue number or prefixes
like `fix/` or `feature/`.

```
$ git switch stable
$ git pull upstream
$ git switch -c short-descriptive-name
```

## Investigate, Code, and Commit Changes

Figuring out what to change can be as much of a challenge as figuring out how to
change it. If an issue includes a minimal reproducible example, you can try
running that with a debugger to track down the problem; or you may need to
formulate your own example script. Writing a test first to demonstrate the
desired behavior, then working to make the test pass, is another strategy.

Make your changes and commit them. Committing as you work is fine, but can get
messy. Try to make each commit a logical chunk of work. If your PR includes many
commits, the maintainers may decide to squash it into a single commit when
merging.

Commit messages should start with a short (<= 50 characters) first line. More
detail can be included, with a blank line separating it from the first line,
wrapped at 72 characters. Don't include issue numbers in the commit message, as
this makes GitHub's UI noisy and hard to follow.

Besides the code itself, a pull request may need tests, docs, and other parts.
See the following guides for each part:

- [Tests](tests.md) - Add tests that demonstrate that your code works, and
  ensure all tests pass. Run `pytest` to run all tests.
- [Static Typing](typing.md) - Run `mypy` to check static typing.
- [Documentation](docs.md) - If behavior has changed somehow, check if any
  documentation pages or docstrings need to be updated.
- [Changelog](changes.md) - Adding a change log entry is optional. A maintainer
  will write one if you're not sure how to. Don't add an entry for changes that
  only affect documentation or tool config.
- [Style](style.md) - pre-commit automatically applies lint and format checks.

### Multiple Authors

Git commit info only includes one author. If you are working with someone else,
you can add one or more `co-authored-by: name <email>` lines to the bottom of
each commit. GitHub will give you and all co-authors credit.

### Syncing with Upstream

If more changes are merged into the project while you're working, you may need
to update your branch to incorporate those changes. Remember to merge from the
same target branch you originally branched off of. You can also `rebase` instead
of `merge`, which is more complicated but produces nicer history.

```
$ git fetch upstream
$ git merge upstream/stable
# or
$ git rebase -i upstream/stable
```

If code you changed was also changed upstream, you'll need to resolve merge
conflicts. Many IDEs, including PyCharm and VS Code, have a UI for resolving
conflicts. There are also standalone merge tools as well. After resolving
conflicts, add and continue the merge.

```
$ git add -u
$ git merge --continue
# or
$ git rebase --continue
```

See [Help with Git](git.md) for more information about rebasing.

## Create the Pull Request

Use the GitHub CLI to start submitting your work as a pull request. Specify the
target branch with `-B`. This is the same branch you branched off of at the
start. The `stable` branch is the target for bug and documentation fixes,
otherwise the target is `main`.

```
$ gh pr create --web --base stable
```

Include the following information in your post:

-   Write a short descriptive title about the change you made.
    -   Do not include prefixes such as "\[fix]"; maintainers will apply real
        tags as needed.
    -   Do not include issue numbers in the title.
-   Describe the change and how it addresses the issue.
-   Link to relevant issues or previous PRs, one per line. Prefix an issue with
    "fixes" to close it with the PR. For example, "fixes #123", "continues
    #123", etc.

Open the PR in "draft" mode. Click the dropdown arrow on the green "Create pull
request" button and select "Create draft pull request". Changes to a draft PR
will not send notifications to everyone watching the project until it is marked
as ready.

## Review and Merge

Once you feel your PR is ready, click the "Ready for review" button. Maintainers
and other experienced contributors may leave review comments. You can push more
commits to address these comments. CI will run tests against the last commit;
you can click to see the logs and address any failures.

Be aware that GitHub allows random people to leave comments and reviews, which
can often be low quality. If you're unsure about a comment, check if GitHub
shows a tag like "owner", "member", or "contributor" next to the user's name. If
not, and the suggestion doesn't seem good, you can ignore it.

Maintainers also have the ability to push commits to your PR. They may choose to
use this for minor changes, or for changes they feel they're in a better
position to make. It's common for maintainers to add or rewrite the change log,
make style changes, and to rebase or squash commits.

This process may take a long time, as maintainers have limited availability
across many projects. Please be patient.

When a maintainer feels the PR is ready, they'll merge it. Or, after more review
of the issue and PR, they may decide to reject the issue or PR. It can be
discouraging to see your work unmerged, but either way doing the work gave you
experience and helped the maintainer make a decision.

Once the PR is merged, the corresponding issue will be closed as well. Both the
issue and PR will be marked with a milestone indicating the future release
that will contain it. You can watch a repository's releases to get notified when
that happens.
