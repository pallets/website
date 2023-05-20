# Triaging Issues

Keeping our backlog organized is extremely helpful. Adding context to issues and
identifying duplicate or previous work helps maintainers and contributors know
what to focus on. It can be difficult to keep track of and to know what calls to
make; this page is a loose collection of guidelines to keep in mind. Close
issues or ask for clarification as needed.

Determine if the issue is with the Pallets library. Issues with the user's own
code should be asked as [questions][] instead, use the "Convert to
discussion" link at the bottom of the sidebar. Issues with another library,
often indicated by a traceback pointing to other code, should be reported to
that library instead.

[questions]: questions.md

Issues in Flask are often actually issues in Werkzeug, or another dependency.
Use the "Transfer issue" link at the bottom of the sidebar to move the issue to
the correct repository.

Issues should succinctly describe the issue, such as an error or expected
behavior, and include a minimal reproducible example. A minimal example should
use only the Pallets library, not other dependencies or setup unless absolutely
necessary. Check that the example reproduces the issue being reported.

Edit issue and PR descriptions to improve their clarity, such as fixing
spelling, grammar, and code highlighting. The title should describe the issue
succinctly and directly, without "tags" like `[feature]`, and without versions.

Search for existing issues. Searching excludes closed issues by default, and
users often miss this, especially when reporting bugs after new releases. Close
duplicate issues with a link to the duplicate. If an issue should remain open,
it's still useful to link to relevant prior discussions and PRs. If the issue
is with another library, try check if it's already been reported there and link
that, or suggest that the user does so.

Add tags to indicate what component the issue is related to. We don't use a
"bug" or "feature" tag, but we do use tags like "docs", "debugger", "windows",
etc. This helps find related issues later. Creating tags and tagging previous
issues can also be helpful.

Add a milestone to indicate what version the issue will be addressed in, or that
the PR will be present it. It can be difficult to know this ahead of time, but
once it is known make sure it is recorded. If a milestone does not exist for the
next version yet, create one.

Some issues may be closed by our policies published on this site. Issues with
deprecations and removals should be linked to [Version Policy][]. Issues asking
for a new release should be linked to [Release Policy][]. If a user posts a
security issue publicly, link to [Security Policy][] and ping a core maintainer.

[Version Policy]: ../versions.md
[Release Policy]: ../releases.md
[Security Policy]: ../security.md
