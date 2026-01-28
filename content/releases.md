# Release Policy

Each version published to PyPI has a corresponding tag in the repository, and a
GitHub release page associated with the tag. GitHub milestones are used to track
which issues and PRs are associated with a given release, as well as listing in
the change log.

See our [Version Support Policy](versions.md) as well.

## Notifications

PyPI provides an RSS feed of [release notifications] for each project. You can
find it at the top of the "Release history" tab on the project's page.

[release notifications]: https://pypi.org/help/#project-release-notifications

GitHub sends a notification each time a release page is created. You can click
"Watch" on a repository and customize to only receive release notifications. It
also provides an Atom/RSS feed, by appending `.atom` to the releases page URL.

Seeing the version on PyPI or the GitHub release page indicates that the version
has been released. Tags are used to trigger the build process, and may be pushed
again if issues come up during the release workflow. Therefore, you should not
rely on git tags to indicate that the release has been published.

## Schedule

The Pallets team works on releases as their time permits. No one works full time
on the projects, so we do not promise any particular release schedule.

Feature releases usually happen once or twice a year, depending on how much
attention a project is getting.

After a new feature release, fix releases will typically wait a few extra days
before publishing. This is to try to reduce the number of releases if new issues
are being reported.

## Security

Building and publishing releases is automated with GitHub workflows and PyPI's
[Trusted Publisher] authentication. Team members on GitHub and PyPI are
required to have 2FA enabled.

[Trusted Publisher]: https://docs.pypi.org/trusted-publishers/
