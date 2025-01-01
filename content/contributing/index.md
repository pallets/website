# Contribute to a Pallets Project

Thank you for considering contributing to Pallets! There are many ways to
contribute to an open source project, see the next section for more ideas.

If you would like to ask a question or open an issue or feature request, see
these guides:

-   [Ask a Question](questions.md), which also covers how to contribute by
    answering questions.
-   [Report an Issue](issues.md)
-   [Report a **Security** Issue](../security.md)
-   [Request a Feature](features.md)

If you would like to fix an issue or implement a feature, see these guides:

-   [Quick Reference](quick.md) If you're already familiar with contributing,
    this provides an essential overview of the following guides.
-   Start Here: Detailed Development Environment Setup - Coming Soon
-   [Create a Pull Request](pr.md)
-   Write and Run Tests - Coming Soon
-   Static Type Checks - Coming Soon
-   [Edit and Build Documentation](docs.md)
-   Changelog Style - Coming Soon
-   Linting and Formatting - Coming Soon

If you're getting more involved as a community or team member, see these guides:

-   [Triaging Issues](triage.md) covers many of the things the team looks for in
    good issue reports and requests.
-   Reviewing and Merging PRs - Coming Soon
-   Project Layout - Coming Soon, explains our standard project structure, tools,
    and configurations.
-   Git Techniques - Coming Soon, talks about various git behaviors and commands.
-   [Making a Release](release.md)

You can also support us by [making a donation](../donate.md).

## What to Work On

Anyone is welcome to work on any open ticket in any project's issue tracker,
without asking first. Before starting, check if anyone else is assigned to the
issue, or if there are any linked open pull requests. Look through the issue for
that information as well as discussion and other linked issues for context.

Besides the core Pallets projects, there is an entire [ecosystem] of extensions
built on top of them. We also have our own dependencies that we use for our
[development environment]. Improving the ecosystem we're part of is a great way
to contribute to Pallets.

[ecosystem]: ../ecosystem.md
[development environment]: layout

Writing code is not the only way to contribute to an open source project. Other
activities are just as helpful. Some ideas that are too broad for individual
issues include:

-   Improve this contributing guide!
-   Improve documentation.
    -   Identify common and popular questions from Stack Overflow. We want users
        to find official information from our documentation first. Perhaps we
        need a new page for a topic, or need to mention a specific error
        message.
    -   Add or improve translations. We also want to improve the workflow around
        updating and publishing translations.
    -   Our documentation is extensive, but it's been written over a long period
        of time by many people. It could use the attention of people with
        technical writing and editing skills.
-   Improve how tests are organized and written to use modern pytest idioms.
    -   Some files have grown very large, or tests are not grouped well, or
        still use `unittest` idioms. Perhaps tests can be split into more files,
        or use pytest's parametrization feature.
    -   Improve test coverage by adding tests for lines and branches that are
        not covered.
-   Improve static type annotations. We target mypy primarily, but would also
    like to improve compatibility with pyright. We also want to ensure we are
    using types correctly, and add tests.
-   Answer questions on GitHub Discussions and our Discord chat server.
    Referencing canonical sources and providing explanation beyond the immediate
    answer creates resources for others to find later and enables them to answer
    in turn.

## Get Help Contributing

If you need help with the contributing process beyond the guides here, or want
to discuss an issue or pull request you're working on, use the `#contributing`
channel on our Discord chat server: <https://discord.gg/pallets>.

You can also write comments on the issue or pull request. After getting help or
researching about an issue, it's helpful to leave a comment there in order to
keep public notes or help the next contributor.

## Join the Team

We are always looking for people interested in joining the team and contributing
long term. If you've established yourself as a member of the community, either
by contributing here or to the ecosystem, and would like to take on more
responsibilities, please get in touch.
