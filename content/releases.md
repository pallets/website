# Release Policy

Each version published to PyPI has a corresponding tag in the repository, and a
GitHub release page associated with the tag. GitHub milestones are used to track
which issues and PRs are associated with a given release, as well as listing in
the change log.

See our [Version Support Policy](versions.md) as well.

## Notifications

PyPI provides an RSS feed of [release notifications][] for each project. You can
find it at the top of the "Release history" tab on the project's page.

[release notifications]: https://pypi.org/help/#project-release-notifications

GitHub sends a notification each time a release page is created. You can click
"Watch" on a repository and customize to only receive release notifications. It
also provides an Atom/RSS feed, by appending `.atom` to the releases page URL.

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
[Trusted Publisher][] authentication. Team members on GitHub and PyPI are
required to have 2FA enabled.

[Trusted Publisher]: https://docs.pypi.org/trusted-publishers/

[Supply-chain Levels for Software Artifacts (SLSA)][slsa] is a relatively new
framework for build and distribution security. We are gradually adopting it as
support and understanding in the Python community grows.

[slsa]: https://slsa.dev/

The context of each build is recorded and signed as SLSA provenance. The
provenance file can be found on the GitHub release page, usually called
`multiple.intoto.jsonl`. Eventually, PyPI will support uploading and displaying
verification for these files. For now, they can be verified manually using
[slsa-verifier][].

[slsa-verifier]: https://github.com/slsa-framework/slsa-verifier
