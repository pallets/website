# Asking and Answering Questions

Don't use the issue tracker to ask questions. The issue tracker is a tool to
report and address bugs and feature requests in the project itself. Use one of
the following resources for questions about using our libraries or issues with
your own code:

-   First, search the web with your preferred search engine, giving the project
    name and a specific search term such as an error message.
-   Ask in the `#questions` channel on our Discord chat:
    <https://discord.gg/pallets>.
-   Use the project's GitHub Discussions tab for long term discussion or
    larger questions. Each project has its own Discussions tab. For example,
    Flask's is here: <https://github.com/pallets/flask/discussions>.

## How to Ask

Try to keep your question focused on using our libraries, not other libraries.
For example, we'll probably be able to answer a question about integrating
SQLAlchemy with Flask, but ask questions about using SQLAlchemy itself in that
project's spaces instead.

When using Discord, use the "Start thread" feature to create a space for your
question. Don't ping users unless you've already established a current
discussion with them. Don't ping users on every reply. Both of these behaviors
are disruptive and will not help you get answers.

Try to keep your question specific. Asking broad questions will probably result
in broad and less helpful answers. Asking how to get started will probably
result in being pointed to existing documentation and tutorials.

Include a [minimal reproducible example] that demonstrates the problem you're
asking about. Start from scratch and build up the minimum code necessary to show
the specific thing you're doing and its output or error. Linking to a full
project or requiring a complex setup will probably dissuade most answerers.

[minimal reproducible example]: https://stackoverflow.com/help/minimal-reproducible-example

Be aware of the [XY Problem][xy]. It can be easy, especially when learning
something new, to convince yourself you need to solve something a certain way,
while missing that the root problem is something else. Be open to this
possibility, as others with more familiarity with the project might point it out
to you.

[xy]: https://en.wikipedia.org/wiki/XY_problem

## How to Answer

A great way to contribute is to answer questions asked on Discord or the
project's GitHub Discussions tab. The more people answer helpfully, the more
people will want to ask and participate, and our community will grow.

Try to answer questions directly and politely. After answering the
immediate question, it's fine to suggest other improvements, or ask followup
questions. Avoid being overwhelming or judgemental. Avoid phrases like "just do this", "it's obvious",
"why would you do that", etc. Remember, everyone is at a different stage of
learning, and you were there once as well.

Try to explain why your answer works rather than only saying what to do. Linking
to specific documentation along with your answer provides a helpful future
reference. For example, "You need to temporarily push an app context so Flask
knows what to access, here's how..." is more helpful than a plain "Use a
`with app.app_context()` block."

If you notice that a question is asked often, that could be an indication that
we should improve our documentation about that topic. Consider reporting an
issue or writing a PR in that case.

Remember, you're answering questions for fun, you are not obligated to perform
any amount of work. You do not need to participate in every question. If you're
not familiar with a topic, don't like how a question was asked, or don't have
time, you can leave it to someone else to pick up.

Be aware of the "Asking" section above. If a new user doesn't provide enough
detail or isn't clear, gently point them towards that. If a user isn't getting
it, disengage rather than having a prolonged back-and-forth. If you believe
someone is being disruptive or taking up too much attention, message moderators
privately.
