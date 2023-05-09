# Hardy Pre-Commit Hooks

A collection of pre-commit hook scripts, written for me, mostly by me (with an
assist from two AIs, ChatGPT and CodePilot).

See also: https://github.com/pre-commit/pre-commit

## Scripts

[commit-msg-sentiment.py](pre_commit_hooks/commit-msg-sentiment.py)
: disallow negative sentiment in commit messages

## How to install

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/hardyoyo/hardy_pre_commit_hooks
    hooks:
    -   id: commit-msg-sentiment.py
```

## License
[MIT](./LICENSE)