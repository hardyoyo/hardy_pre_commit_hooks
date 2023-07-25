# Hardy Pre-Commit Hooks

A collection of pre-commit hook scripts (OK, well, not quite, keep reading), 
written for me, mostly by me (with an assist from two AIs, ChatGPT and GitHub Copilot).

See also: https://github.com/pre-commit/pre-commit

## Scripts

[commit-msg-sentiment.py](pre_commit_hooks/commit-msg-sentiment.py)
: disallow negative sentiment in commit messages

### Yep, that's a commit-msg git hook script

[Pre-Commit](https://github.com/pre-commit/pre-commit) is a really nice
framework, and it has lots of extra goodies you should definitely check out and
use. Pre-commit is capable of installing commit-msg-sentiment.py as a commit-msg Git
Hook script, and has been configured to do so.

## How to install

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/hardyoyo/hardy_pre_commit_hooks
    rev: v1.3
    hooks:
    -   id: commit-msg-sentiment.py
```

And then ask pre-commit to install the commit-msg hook script to your repository:

```
pre-commit install --hook-type commit-msg
```

## Known issue: pre-commit doesn't install a working commit-msg git hook script

This is probably an issue with my configuration for pre-commit. Until I work out
exactly what the issue is, here's the workaround: after running the install
command above, you'll need to manually replace the `.git/hooks/commit-msg` script
installed by pre-commit with the [commit-msg](commit-msg) script in this repository.

## How to test

To run the test suite, cd to the tests folder, then run
```bash
python3 ./test_commit_messages.py
```

You can also test your own example commit messages whenever you wish with:

```
echo "this is a dumb commit message" | commit-msg-sentiment.py
```

This is useful when you are adjusting your configuration (see below).

## Configuring

There are a few environment variables you can set to affect how
commit-msg-sentiment.py functions:

**MIN_COMMIT_MSG_LENGTH** (defaults to 120)
Mininum number of characters at which we'll switch to using TextBlob instead of
Affin for sentiment analysis. TextBlob doesn't handle short strings very well,
Affin does better. You may need to adjust this number to suit your own commit
message style.

**SENTIMENT_THRESHOLD** (defaults to 0.01)
Both Affin and TextBlob have a similar concept of a Sentiment Threshold. You can
tinker with this number if you like, but 0.01 seems to be the sweet spot for
typical commit messages.

**REJECT_MSG**
You can customize the message that is used when rejecting a commit for negative
sentiment. But, do try to be kind to yourself. That's the whole point of this.

## The Story

I started thinking about this project a few years ago. I was collaborating with
a new team, on an unfamiliar codebase. And I made a commit on my own personal
branch, thinking I was fixing a bug **I** had introduced. I was wrong, it was my
colleague. Someone who I trusted and appreciated. And I had to see their reaction
to my mouthy, ill-considered commit message. I just wasn't used to the idea of
other people seeing my commit messages, even though, of course anyone can see
them. I still remember the sinking feeling, and the shame. And I thought, you
know, someone should make a git hook script to reject grumpy commit
messages. That would save others (and, possibly me) from that same awful
feeling, of disappointing a friend.

So, I gave ChatGPT a chance to design a pre-commit hook script, and the skeleton
of the implementation here is from that AI. I did all the work of putting things
together, and evaluating the various sentiment analysis framework options.
TextBlob turned out to be the most dependable for longer commit messages. But it
offered lots of false-positives on short commit messages. I experimented a bit
with various word-based approaches, then settled on Afinn as it uses a
word-based approach, and has a similar threshold mechanism as TextBlob.

GitHub Copilot gets a shout-out because during the final work of putting everything
together, I relied on its syntax hints to finish up the script and the tests.
Some of the neutral commit messages are suggestions from Copilot.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
[MIT](./LICENSE)
