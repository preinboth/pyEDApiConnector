# Guidelines for contributing to EdApiConnector

## Work on Issues

If you are not part of the core development team then you should only be performing work that addresses an open issue.

So, if what you think needs doing isn't currently referred to in an
[open issue](https://github.com/preinboth/pyED-Api-Connector/issues),
then you should first [open an issue](https://github.com/preinboth/pyED-Api-Connector/issues/new/choose).
**Please use the correct template if applicable**.

## Check with us first

Whilst we welcome all efforts to improve the program it's best to ensure that you're not duplicating, or worse,
wasting effort.

There is sometimes a misconception that Open Source means that the primary project is obliged to accept Pull Requests.
That is not so. While you are 100% free to make changes in your own fork, we will only accept changes that are
consistent with our vision for EdApiConnector. Fundamental changes in particular need to be agreed in advance.

---

## Text formatting

The project contains an `.editorconfig` file at its root. Please either ensure
your editor is taking note of those settings, or cross-check its contents
with the
[editorconfig documentation](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties)
, and ensure your editor/IDE's settings match.

---

## General workflow

1. You will need a GitHub account.
1. Fork the repository on GitHub into your account there (hereafter referred to as 'your fork').
1. In your local copy of *your* fork create an appropriate WIP branch.
1. Develop the changes, testing as you go (no we don't have any actual tests yet).
    1. Be as sure as you can that the code works as you intend and hasn't introduced any other bugs or regressions.
    1. Test the codebase as a whole against any unit tests that do exist, and add your own as you can.
    1. Check your code against flake8 periodically.
1. When you're sure the work is final:
    1. Push your WIP branch to your fork (you probably should have been doing this as you worked as a form of backup).
    1. Access the WIP branch on your fork on GitHub and create a Pull Request. Mention any Issue number(s) that it
       addresses.
1. Await feedback in the form of comments on the Pull Request.

**IMPORTANT**: Once you have created the Pull Request *any changes you make to that WIP branch and push to your fork
will be reflected in the Pull Request*. Ensure that *only* the changes for the issue(s) you are addressing are in
the WIP branch. Any other work should occur in its own separate WIP branch. If needs be make one branch to work in
and another for the Pull Request, merging or cherry-picking commits as needed.

---

## Git commit conventions

* Please use the standard Git convention of a short title in the first line and fuller body text in subsequent lines.
* Please reference issue numbers using the "hashtag" format #123 in your commit message wherever possible.
  This lets GitHub create two-way hyperlinks between the issue report and the commit.
  [Certain text](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
  in a PR that fixes an issue can auto-close the issue when the PR is merged.
  Note the caveats about the extended forms being necessary in some situations.
* If in doubt, lean towards many small commits. This makes git bisect much more useful.
* Please try at all costs to avoid a "mixed-up" commit, i.e. one that addresses more than one issue at once.
  One thing at a time is best.

---
