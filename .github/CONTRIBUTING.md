# Contributing Guidelines

Want to contribute to this repo? Great! We  :heart:  contributions. Just make sure to follow these guidelines.
Read both the [general guidelines](#general-guidelines) and the [coding style guidelines](#coding-style-guidelines).
By making a contribution, in any form (including, but not limited to, Issues and Pull Requests), you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Where should I contribute?

In this repository, silly! In all seriousness, we did not create this projects, the fine folks at UPC in Barcelona did. This fork is being tailored for WashU's upcoming 2022 Hackathon, and is a fork of a fork of UPC's HackAssistant. If we need to add a big feature, consider adding it to the upstream branch.

> NOTE: Reach out to them post-hackathon about updating the original project

### Why are we two layers deep?

From what we can tell, Hack UPC made the original project though the repo hasn't been touched for years. That's the version that's linked on MLH's website, but it seems deprecated. We found that there was a modern version available on GitHub that Hack UPC used back in December 2021 to host a hackathon. Since UPC's specific verison is more recently updated, we decided to fork theirs instead of merging 3 years worth of changes between their updated version and the deprecated repository. Thanks guys :heart:

## General Guidelines

### New Feature or a Bug Fix?

0. Create a GitHub issue for what you're doing so we can track what's currently being worked on
1. Fork the repo (can be skipped if you're in the Hack WashU GitHub org)
2. Create a new branch with a descriptive name of the feature or the bug you are fixing.
3. Push your new branch to your remote and mention in the issue that you've started work on the feature/fix and link to your branch.
4. Make changes and commit them. Your commit messages should be descriptive and imperative. Read [this](http://who-t.blogspot.com/2009/12/on-commit-messages.html) for guidelines.
5. Create a pull request with a descriptive title. Clearly document any changes you made. You should be able to explain why you made those changes.

<!-- ### Working on the Next Release?

1. Work on the `dev` or `develop` branch
2. Create a pull request with a descriptive title. Clearly document any changes you made. You should be able to explain why you made those changes. -->

## Coding Style Guidelines

> NOTE: We're not enforcing this right now -- we need to get an MVP out ASAP. This is something to come back to between registration opening and the hackathon starting.

This project applies the same coding style than [Django Project](https://docs.djangoproject.com/en/1.11/internals/contributing/writing-code/coding-style/) which follows almost all [PEP-8](https://www.python.org/dev/peps/pep-0008/) coding guidelines.

We allow up to 119 characters/line as this is the width of GitHub code review; anything longer requires horizontal scrolling which makes review more difficult. This check is included when you run flake8. Documentation, comments, and docstrings should be wrapped at 79 characters, even though PEP 8 suggests 72.

All of this is enforced with Travis CI. All PRs will need to success on Travis before being merged.

<!-- TODO: Consider Travis CI? -->

## Commit Message Guidelines

Commit Guidelines inspired by [Gnome Commit Guidelines](https://wiki.gnome.org/Git/CommitMessages).

Those are only general-purpose recommended guidelines, depending on the context of each PR the following rules can vary.

Remember: the commit message is mainly for the other people, so they should be able to understand the changes made at any point in time.

### Example

```
short explanation of the commit

Longer (optional) explanation explaining exactly what's changed and why instead of how,
whether any external or private interfaces changed, what bugs were fixed (with bug
tracker reference if applicable) and so forth. Be concise but not too brief. Avoid writing long lines, use newlines when necessary.

[Reference to the issue solved, if any]
```

### Details

- First line (the brief description) must only be one sentence in imperative mood. The message should be concise, less than 50 characters if possible. Do not end it with a period.
- The long explanation is optional, although it is encouraged to be written if it helps clarify the issue tackled. Explain the "why", not the "how" there and try to wrap every line at 72 characters. Also, keep a blank like between the first line and the long explanation.
- Remember to commit your code with a [username](https://help.github.com/articles/setting-your-username-in-git/) and [email](https://help.github.com/articles/setting-your-email-in-git/).
- If there is an issue created for this commit, link it at the end of the commit message, in a new line. The issue should follow the [GitHub guidelines](https://help.github.com/articles/closing-issues-via-commit-messages/#closing-an-issue-in-the-same-repository).
