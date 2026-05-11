# Git Commands Reference

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Initialize & Clone
```bash
git init                        # Initialize a new repo
git clone <url>                 # Clone a remote repo
```

## Staging & Committing
```bash
git status                      # Check working tree status
git add <file>                  # Stage a file
git add .                       # Stage all changes
git commit -m "message"         # Commit staged changes
git commit --amend              # Modify the last commit
```

## Branching
```bash
git branch                      # List branches
git branch <name>               # Create a branch
git checkout <name>             # Switch to a branch
git checkout -b <name>          # Create and switch to a branch
git merge <name>                # Merge branch into current
git branch -d <name>            # Delete a branch
```

## Remote
```bash
git remote -v                   # List remotes
git remote add origin <url>     # Add a remote
git push origin <branch>        # Push to remote
git pull origin <branch>        # Pull from remote
git fetch                       # Fetch remote changes
```

## Logs & Diff
```bash
git log                         # View commit history
git log --oneline               # Compact commit history
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
```

## Undo
```bash
git restore <file>              # Discard working directory changes
git reset HEAD <file>           # Unstage a file
git reset --soft HEAD~1         # Undo last commit, keep changes staged
git reset --hard HEAD~1         # Undo last commit, discard changes
git revert <commit>             # Create a new commit that undoes a commit
```

## Stash
```bash
git stash                       # Stash current changes
git stash pop                   # Apply and remove latest stash
git stash list                  # List all stashes
git stash drop                  # Remove latest stash
```

## Tags
```bash
git tag                         # List tags
git tag <name>                  # Create a lightweight tag
git tag -a <name> -m "msg"      # Create an annotated tag
git push origin <tag>           # Push a tag to remote
```
