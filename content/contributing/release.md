# Creating a Release

This document explains the process of creating a release and everything you need
to do and check along the way. Despite the length of this document, this is
intended to be an easy process once you're used to it. Be sure to read it
through the first time you do a release. Next time, you can use this abbreviated
checklist.

1.  Decide to make a release.
2.  Ensure the change log has entries for each user-facing non-docs change, with
    links to the related issue reports.
3.  Ensure each issue and PR is in the milestone.
4.  Create a `release-A.B.C` branch.
5.  Change "Unreleased" to "Released YYYY-MM-DD" in `CHANGES.md`.
6.  Remove the ".dev" suffix from the version in `pyproject.toml`.
7.  Commit `git commit -am 'release version A.B.C'` and create a PR.
8.  Tag `git tag -am 'release version A.B.C' A.B.C` and push
    `git push origin A.B.C`.
9.  Watch the tests pass and build jobs begin.
10. Edit the generated draft release page with our standard message template.
11. Approve the upload job.
12. Merge the PR. Use "create a merge commit", not "squash" or "rebase"!
13. Close the milestone.
14. Publish the draft release page.
15. Start the next version(s), creating a change log section, bumping the
    version in `pyproject.toml` with the `.dev` suffix.
16. Done!

## Decision

There is no precise way to know that it's time for a release. Ideally, fixes
should be released within a few weeks (perhaps to wait and see if more bugs need
to be fixed), and features should be released perhaps twice a year. We don't
want to overwhelm our users with constant releases or churn, but we also don't
want to delay things forever. Ultimately, it's up to a maintainer to decide that
the time "feels right" for a new release and start the process.

## Preparation

Each project has two branches and milestones that represent the two upcoming
releases. `main` tracks the next feature release, which should have a
corresponding `A.B.0` milestone.  `stable` tracks the next fix release, which
should have a corresponding `A.B.C` (where `C > 0`) milestone.

Each merged PR, and any issues associated with it, should be marked with the
appropriate milestone. This makes it easier to review what changes are ready to
be released, and what may still be blocking a release. If a PR or issue in a
milestone has not been merged yet, you can make the decision to unmark it to
unblock a release.

In each branch, the `CHANGES.md` file should have a section for the upcoming
release. Each PR should have a corresponding entry in the change log (for
user-facing changes only, and not docs). Each entry should link to the
corresponding issue with `` {issue}`number` ``. If a PR doesn't have a
corresponding issue, use `{pr}` instead of `{issue}` for the link. Ideally, this
was part of the PR when it was merged, you should not be creating the entire
change log at the last minute.

Review the milestone and change log to ensure each PR has a change entry, is in
the milestone, and is linked to an issue, which is also in the milestone.

Ensure everything from `stable` has been merged into `main` if you're creating a
feature release.

The tests will be run as part of the release PR, but you can also run `tox`
locally to ensure everything is passing first.

## Start the Release Process

The release process is managed through a PR. This allows you to see that all
tests pass, and that the build passes, by looking at the standard PR checks UI.

1.  Check out the `main` or `stable` branch depending on what release you're
    making.
2.  Check out a new branch with the name `release-A.B.C`, for example
    `release-3.2.0`.
3.  Update `CHANGES.md` to change `Unreleased` to `Released YYYY-MM-DD`, for
    example `Released 2024-08-04`.
4.  Update `pyproject.toml` to change `[project].version`, removing the `.dev`
    suffix and ensuring the version number is correct.
5.  Commit the changes with the message `release version A.B.C`.
6.  Push the branch to the main repository, not a fork, and create a PR.
    -   The PR title will default to the commit message, and the description can
        be empty.
    -   Assign the appropriate milestone to the PR.

After the PR is created, the normal test workflow will run. In the meantime, you
start the build process by pushing a tag.

1.  Tag the release commit you just created. `git tag -am 'release version A.B.C'`
    -   The `-am` creates an annotated tag with a message. Don't forget the `-am`!
2.  Push the tag to the main repository, not a fork. `git push origin A.B.C`

The `publish.yaml` workflow will start to run and you'll see build-related
checks show up in the PR checks UI. First, it builds the sdist and wheel. Then
it creates a draftrelease and uploads the built files to it. Finally, you'll
see it waiting for approval to upload to PyPI. Don't approve it yet, there's
more to do first.

## Prepare the Release Message

Go to the releases for the project, and find the draft release at the top of the
list. Click edit. While editing, you can click "Save draft", but do not click
"Publish" until after the release is complete.

The uploaded files from the previous step will be listed at the bottom. Do they
look right? Do they have the right version? If you're really worried, you can
also download the file and check if the contents look right, but this shouldn't
be needed

Currently, the workflow does not populate the release message, so you'll need to
fill it in. This will be automated in the future. The message has the following
format:

For feature releases, the explanation is:

```markdown
This is the {project} {version} feature release. A feature release may include new features, remove previously deprecated code, add new deprecations, or introduce potentially breaking changes.

We encourage everyone to upgrade. You can read more about our [Version Support Policy][version] on our website.

[version]: https://palletsprojects.com/versions

PyPI: https://pypi.org/project/{pypi name}/{version}/
Changes: https://{project}.readthedocs.io/page/changes/#version-{A-B-C}
Milestone https://github.com/pallets-eco/{project}/milestone/{milestone}?closed=1

{change entries, markdown, replace links}

Please remember, applications _must_ lock their full dependency tree to control when updates are installed and ensure reproducible deployments. Use one of the various project management or lock tools available in the Python ecosystem. Test with warnings treated as errors to be able to adapt to deprecation warnings early.
```

For fix releases, the explanation is:

```markdown
This is the {project} {version} fix release, which fixes bugs but does not otherwise change behavior and should not result in breaking changes compared to the latest feature release.

PyPI: https://pypi.org/project/{pypi name}/{version}/
Changes: https://{project}.readthedocs.io/page/changes/#version-{A-B-C}
Milestone https://github.com/pallets-eco/{project}/milestone/{milestone}?closed=1

{change entries, markdown, replace links}
```

Copy and paste the change log entries from the version's section. You'll need to
replace the `` {issue}`number` `` markup with `#number`. If the change log is
still in `.rst` format, you'll need to make sure it renders correctly in
Markdown, or use a tool like `rst2myst` to convert them. Over time, we plan to
make all change log files Markdown to avoid this issue.

**Never use GitHub's "Generate release notes" feature.** Copying each commit
message/PR title is not helpful compared to the curated change log we produce.
Additionally, the pings it adds for each contribtor can become spammy,
especially if mirrors/bots pick up the release and copy it into other
issues/commits, which _has_ happened in the past.

## Finalize the Release

Approve the upload job. In the PR check status window, click to view the
"pypi-publish" job. You should see a link to "Review pending deployments",
clicking it will open a confirmation window. Select the "publish" item and click
"Approve". You'll see the publish workflow begin. Wait for it to complete
successfully.

Close the milestone. Click the link to the milestone from the PR, click "Edit",
then click "Close".

Merge the PR. **Make sure the "create a merge commit" strategy is selected.**
Using the "sqaush" or "rebase" strategies will cause the tagged commit to be out
of sync with the repo. Remember, you tagged the _specific_ commit in the PR,
squashing or rebasing would re-create that commit so the tag would no longer be
valid. This is recoverable with difficulty, but don't let it happen.

Publish the release page. Go back to the draft release page and click "Publish".
Anyone watching the repository for releases will get a notification.

## Start the Next Version

### After a Fix Release

Optimistically, there won't be another fix release after a fix release, so you
can defer doing all this until at least one issue is reported.

1.  Create a milestone for `A.B.C+1`.
2.  Start the next fix version.
	1.  `git switch stable && git pull`
	2.  Update `CHANGES.md` to add a new section at the top:
		```markdown
		## Version A.B.C+1

		Unreleased
		```
	3.  Update `pyproject.toml` to change `[project].version`. Set it to
        `A.B.C+1.dev`, note the `.dev` suffix.
	4.  Commit the changes with the message `start version A.B.C+1`
	5.  Push this commit, no need to create a PR.
3.  Merge `stable` into `main`. Make sure the new change log section is merged
    _below_ the section for the next feature relase, and that the version isn't
    overwritten.
4.  Push `main`.

### After a Feature Release

Realistically, there will be at least one fix release after a feature release,
and there will be the next feature release as well.

1.  Create a milestone for `A.B+1.0`, the next feature release.
2.  Create a milestone for `A.B.1`, the first fix release.
3.  Fast-forward `stable` to point at `main`. From `stable`:
    `git merge --ff-only main`.
4.  Start the next fix version, as described in the previous section.
5.  Start the next feature version, using the same steps describe in the
    previous section, except on `main`.

## Done!

Congratulations, the release process is complete!
