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
    rev: v1.0
    hooks:
    -   id: commit-msg-sentiment.py
```

## How to test

To run the test suite, cd to the tests folder, then run
```bash
python3 ./test_commit_messages.py
```

## The Story

I started thinking about this project a few years ago. I was collaborating with
a new team, on an unfamiliar codebase. And I made a commit on my own personal
branch, thinking I was fixing a bug **I** had introduced. I was wrong, it was my
colleague. Someone who I trusted and appreciated. And I had to see her reaction
to my mouthy, ill-considered commit message. I just wasn't used to the idea of
other people seeing my commit messages, even though, of course anyone can see
them. I still remember the sinking feeling, and the shame. And I thought, you
know, someone should make a pre-commit hook script to reject grumpy commit
messages. That would save others (and, possibly me) from that same awful
feeling, of disappointing a friend.

So, I gave ChatGPT a chance to design a pre-commit hook script, and the skeleton
of the implementation here is from that AI. I did all the work of putting things
together, and evaluating the various sentiment analysis framework options.
TextBlob turned out to be the most dependable for longer commit messages. But it
offered lots of false-positives on short commit messages. I experimented a bit
with various word-based approaches, then settled on Afinn as it uses a
word-based approach, and has a similar threshold mechanism as TextBlob.

Co-pilot gets a shout-out because during the final work of putting evertything 
together, I relied on its syntax hints to finish up the script and the tests.
Some of the neutral commit messages are suggestions from Co-pilot.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
[MIT](./LICENSE)
