
# 09 – Pull Request Checks

<img src="../../media/github-actions-logo-name.jpg" style="width: 300px" align="right">

> Add automated checks for code quality and correctness using GitHub Actions. Run black and pytest on every pull request.

Set up GitHub Actions to automatically check pull requests. Add workflows for formatting (black, ruff) and automated testing (pytest). Ensure that every change to your codebase is checked before being merged.

- One of the tests could be: run_training.py script sanity (e.g. does it run 1 epoch without error?)
