
## Lab 09 – Pull Request Checks

<img src="../../media/github-actions-logo-name.jpg" style="width: 300px" align="right">

> Add continuous integration (CI) checks to your project using GitHub Actions. Automatically test your code and check formatting every time someone opens a pull request.

### 🎯 Goal

In this lab, you'll:

- ✅ Set up GitHub Actions on your own repository
- ✅ Automatically run PyTest (unit tests) and Black (code formatter)
- ✅ Trigger workflows manually and on pull requests
- ✅ Optionally protect your main branch using CI results

### 🗂️ What’s in this folder

| File                             | Purpose                              |
|----------------------------------|--------------------------------------|
| `data_utils.py`                 | Python module to be tested            |
| `test_dataloader.py`            | A simple PyTest unit test            |
| `checks.yml`                    | A pre-written GitHub Actions workflow |

### 🧩 Part 1 – Run the Workflow Manually

Let’s first run the CI manually to verify that everything works.

#### 🛠️ Step 1: Create your GitHub repo

Use your own repo from previous labs, or make a new one.

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/lab9-checks.git
````

Make sure your working directory includes the provided files:

```
data_utils.py
test_dataloader.py
.github/workflows/checks.yml
```

Then commit and push:

```bash
git add .
git commit -m "Add test and workflow"
git push -u origin main
```

#### ▶️ Step 2: Run the workflow by hand

1. Go to your GitHub repo
2. Click the **Actions** tab
3. Select the `Run tests and format check` workflow
4. Click **"Run workflow"**

You should see it start running. Once it completes, check the output of the two steps:

* ✅ PyTest test runner
* ✅ Black formatting check

If anything fails, the job will be marked red ❌ — fix the problem and push again.

### 🧩 Part 2 – Run Checks on Pull Requests

Now let’s make CI run automatically when you open a pull request.

#### 🛠️ Step 1: Create a new branch

```bash
git checkout -b bad-format
```

Now open `test_dataloader.py` and add this line at the top:

```python
import       sys
```

But **don’t format it nicely** — leave some ugly spacing.

Then commit and push:

```bash
git add .
git commit -m "Break formatting"
git push --set-upstream origin bad-format
```

#### 🔁 Step 2: Open a pull request

1. Go to your GitHub repo
2. Click **"Compare & pull request"**
3. Submit a PR from `bad-format` → `main`

GitHub will now show a CI check running automatically at the bottom of the pull request.

Once it finishes:

* You’ll see ❌ if there’s a formatting or test failure
* You’ll see ✅ if everything passes

Now fix the formatting locally:

```bash
black test_dataloader.py
```

Commit and push the fix:

```bash
git add .
git commit -m "Fix formatting"
git push
```

CI will re-run and (hopefully) pass 🎉

### 🧩 Part 3 – Protect the Main Branch

Let’s now **require that checks pass before merging**.

#### 🛠️ Step 1: Enable branch protection

1. Go to your GitHub repo
2. Click **Settings** → **Branches**
3. Click **“Add branch protection rule”**
4. Fill in:
   * **Branch name pattern**: `main`
   * ✅ Require status checks to pass
   * ✅ Select `Run tests and format check`
   * ✅ Require branches to be up to date
5. Click **Create**

Now GitHub will block any pull request from being merged unless CI passes.

### ✅ Summary

By the end of this lab, you:

* Set up a working GitHub Actions workflow
* Automatically ran Black and PyTest
* Created a pull request and saw checks run
* Protected your main branch using CI results

This is your first step into **real-world software engineering** workflows — where every commit is automatically tested before it’s merged.
