# Request a Feature

If you feel that one of our libraries is missing something, you should request
a new feature for it on the GitHub Issues tab. For example, Flask's is here:
<https://github.com/pallets/flask/issues/>.

The bar for accepting new features into many of our libraries is high. Our
general philosophy is to provide a solid base framework that other libraries can
extend, rather than blessing specific implementations in the core library. A
feature request may be more successful if:

-   If it's not possible to implement as an extension without changes to the
    core.
-   If there is one "correct" way to implement something.
-   If the request is similar to or complements existing behavior.

Before requesting a feature, try to determine if it has already been requested
or implemented. Search existing issues and PRs, including closed issues and
merged PRs. Requests that were previously rejected are likely to be rejected
again unless (or even if) significant new reasoning is presented.

Click the green "New issue" button at the top right to start. Include the
following information in your post:

-   Write a short, descriptive title.
    -   Do not include prefixes such as "\[feature]"; maintainers will apply
        real tags as needed.
-   Describe what the feature should do.
-   Include details such as links to relevant specs or previous discussions.
-   Provide an example of a problem this feature would resolve. Consider if this
    is problem solvable without changes to the library, such as by subclassing
    or using an extension.
