#!/usr/bin/env python3

import os
import sys
from textblob import TextBlob
from afinn import Afinn

# COMMIT-MSG-SENTIMENT.PY
# a post-commit hook to check commit message sentiment, and reject commit if
# negative sentiment is detected. Uses TextBlob to get sentiment polarity score
# for longer commit messages, and Afinn to get sentiment polarity score for
# shorter commit messages.



################################## SETUP ######################################

# Set the minimum length of commit message to check
DEFAULT_MIN_COMMIT_MSG_LENGTH = 15

# Set default threshold for sentiment polarity
DEFAULT_THRESHOLD = 0.01

# Set default reject message
DEFAULT_REJECT_MSG = """
Hmmm... That was a bit negative. Remember, other people will read this message. 
Please try again with a more constructive tone. Here are some guidelines to 
keep in mind:\n
- Be descriptive: Include a brief summary of what was changed in the commit.\n
- Be concise: Keep the message short and to the point.\n
- Be constructive: Use language that is respectful and constructive, even when 
  discussing challenges or issues.\n
"""

# Get minimum commit message length from environment variable, if set
min_commit_msg_length = os.environ.get("MIN_COMMIT_MSG_LENGTH")
if min_commit_msg_length is None:
    min_commit_msg_length = DEFAULT_MIN_COMMIT_MSG_LENGTH
else:
    min_commit_msg_length = int(min_commit_msg_length)

# Get threshold from environment variable, if set
threshold = os.environ.get("SENTIMENT_THRESHOLD")
if threshold is None:
    threshold = DEFAULT_THRESHOLD
else:
    threshold = float(threshold)

# Get reject message from environment variable, if set
reject_msg = os.environ.get("REJECT_MSG")
if reject_msg is None:
    reject_msg = DEFAULT_REJECT_MSG

def reject_commit():
    print(reject_msg)
    sys.exit(1)

def accept_commit():
    sys.exit(0)

afinn = Afinn()

############################# BEGIN MAIN SCRIPT ################################

# Get commit message from file or stdin
if len(sys.argv) > 1:
    commit_file = sys.argv[1]
    with open(commit_file, "r") as f:
        commit_msg = f.read().strip()
else:
    commit_msg = sys.stdin.read().strip()

# for short commit messages, use Afinn to get sentiment polarity score (uses a
# modified threshold, to avoid false positives for short messages)
if len(commit_msg) < min_commit_msg_length:
    sentiment_score = afinn.score(commit_msg)
    if sentiment_score < (threshold-1):
        reject_commit()
    else:
        accept_commit()

# for longer commit messages, use TextBlob to get sentiment polarity score
blob = TextBlob(commit_msg)
sentiment_score = blob.sentiment.polarity

# Reject commit if sentiment score is below threshold
if sentiment_score < threshold:
    reject_commit()
else:
    accept_commit()
