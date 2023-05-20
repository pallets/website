# Security Policy

If you believe you have identified a security issue with any Pallets project,
**do not open a public issue**. To responsibly report a security issue, please
[draft a private security advisory][advisory] on the relevant GitHub repository.
Further collaboration can be done through the advisory workflow. Alternatively,
you may email security@palletsprojects.com.

[advisory]: https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability#privately-reporting-a-security-vulnerability

Include as much detail as necessary in your report. A minimal reproducible
example helps the maintainers identify and address the issue.

The currently supported feature branch will receive security fixes. A backport
to the previous feature branch will be considered based on usage and severity
upon request.

As part of the security advisory workflow, we will obtain a CVE. Once the fix
is released, we will publish the advisory and CVE as well.

## Before Reporting

These categories will generally not be considered issues:

* The Werkzeug and Flask development server, debugger, and reloader.
  Documentation and startup messages already clearly indicate that these are
  intended for local development only.
* Use of Jinja and MarkupSafe HTML escaping in other contexts, such as
  JavaScript.
* Insecure configuration or code in a project *using* our libraries. This should
  be reported to the relevant project instead.
