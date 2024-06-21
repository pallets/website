# Version Support Policy

We encourage you to always use the latest stable version of our libraries, other
dependencies, and Python.

The latest feature version for each project will receive bug and security fixes.
Older feature versions will not receive fixes. Depending on severity and level
of effort, security fixes _may_ be backported one version upon request.

When a release is made, it supports all Python versions that are not within six
months of end of life (EOL). See [Python's EOL calendar][eol] for timing.

[eol]: https://devguide.python.org/versions/

See our [Release Policy](releases.md) as well.

## Version Format

Each project uses versions that follow the [PEP 440][] format. Stable releases
have three numbers, `A.B.C`. We follow a version scheme similar to Python
itself.

* The `A` number is considered a "milestone" release. It increases rarely, and
  indicates a significant change in the project's structure or capabilities.
* The `B` number is considered a "feature" release. Increasing this number
  indicates adding new features, and may deprecate existing code or remove
  previously deprecated code.
* The `C` number is considered a "fix" release. Increasing this number indicates
  changes to fix bugs or security issues, and will not intentionally break
  public APIs.

## Public API, Deprecations, and Removals

Any classes, functions, attributes, etc. that are documented in the online
documentation (rather than only the source code) are considered public API.
Changes, additions, deprecations, removals, and fixes will be mentioned in the
change log for each version.

We do our best to avoid breaking documented APIs without first showing deprecation
warnings. These warnings will mention the thing that is deprecated, the version
it will be removed, and an alternative if applicable. After a deprecation
warning is added in one feature release, the next feature release may remove
that code.

As we continue to maintain and evolve the libraries, we may need to change or
remove public APIs. We are aware of the widespread and historic use of our
libraries, and do not take these changes lightly. We do not hold back changes
only to accommodate existing code, but we will work with the community to help
migrations.

## Pinning Versions and Constraints

When writing an application, you *must* use a tool like [pip-compile][] to pin
your application's full dependency tree. This gives you reproducible
deployments, allowing you to control when you get updates.

[pip-compile]: https://pypi.org/project/pip-tools/

Be sure to run your tests with deprecation warnings treated as errors so that
you get notified of those types of changes early.

When writing a library, you *should not* use exact (`==`) or maximum (`<`, `<=`)
constraints on dependency version unless you know that a given branch or the
project as a whole will never support later versions. These strict constraints
cause dependency resolution issues for applications using those projects, and
should instead be solved by the application pinning _their_ dependency tree as
described above.

## Not SemVer

We do not assign "SemVer" meanings or guarantees to versions. In general, you
must not assume that any project that uses a three-number implies SemVer. Our
policy described above does use similar ideas. It may help to think of our
versions as `major.major.patch` if you need to use SemVer in other contexts.

Please see any of the following resources for more information:

* <https://hynek.me/articles/semver-will-not-save-you/>
* <https://www.youtube.com/watch?v=WSVFw-3ssXM&t>
* <https://snarky.ca/why-i-dont-like-semver/>
* <https://caremad.io/posts/2016/02/versioning-software/>
* <https://bernat.tech/posts/version-numbers/>
* <https://iscinumpy.dev/post/bound-version-constraints/>

[PEP 440]: https://peps.python.org/pep-0440/
