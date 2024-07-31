# Security Policy

If you believe you have identified a security issue with a Pallets or
Pallets-Eco project, **do not open a public issue**. To responsibly report a
security issue, use GitHub's [security advisory system][gh-docs]. From the
project's repository, click "Security" at the top, then click "Advisories" at
the left, then click the green "New draft security advisory" button.
Alternatively, you may email [security@palletsprojects.com](mailto:security@palletsprojects.com),
and we will convert that to a GitHub security advisory.

Be sure to include as much detail as necessary in your report. As with reporting
normal issues, a minimal reproducible example will help the maintainers address
the issue faster. Information about why the issue is a security issue is also
helpful. If you are able, you may also provide a fix for the issue.

A maintainer will reply acknowledging the report and how to continue. We will
obtain a CVE id as well, please do not do this on your own. We will work with
you to attempt to understand the issue and decide on its validity. Maintainers
are volunteers working in their free time, and therefore cannot guarantee any
specific timeline. Please be patient during this process.

The current feature release will receive security fixes. A backport to the
previous feature branch may be considered upon request based on usage information
and severity, but is not guaranteed.

[gh-docs]: https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/creating-a-repository-security-advisory

## Before Reporting

The following categories will generally not be considered security issues. You
may still err on the side of caution and make a private report first, but we
may close it or ask you to report a regular issue instead.

* The Werkzeug and Flask development server, debugger, and reloader.
  Documentation and startup messages already clearly indicate that these are
  intended for local development only.
* Use of Jinja and MarkupSafe HTML escaping in other contexts, such as JavaScript.
* Use of SHA-1 in ItsDangerous. SHA-1 is not vulnerable when used as an
  intermediate step in HMAC, and ItsDangerous can be configured to use another
  algorithm when needed.
* Insecure configuration or code in a project *using* our libraries. This should
  be reported to the relevant project instead.
* Regular expression performance, often referred to as "ReDoS". Deployed
  applications should use standard/recommended resource limits offered by their
  server software and hosting service. You may report this as a regular
  performance issue instead of a security issue.
* Automated reports from vulnerability scanners or "AI" tools. Please make it
  clear that you understand what you are reporting and have put personal time
  into crafting the report.
* Do not report something that has already been fixed and released; check the
  project's change log. Getting a notification from your security scanner that
  you need to update is not itself a new vulnerability to report.
