import subprocess

def test_negative_commit_messages():
    messages = [
        "This is a terrible commit message.",
        "I guess this might work, but it's not great.",
        "Who wrote this garbage?",
        "Not sure why anyone would want to use this.",
        "Why do I even bother?",
        "Can't believe I wasted my time on this.",
        "This code is a mess.",
        "This is a mess.",
        "Ugh, this is so frustrating.",
        "What were they thinking when they wrote this?",
        "This is a disaster.",
        "This is a nightmare.",
        "This is a joke.",
        "This is a waste of time.",
        "This is a waste of money.",
        "This is a waste of energy.",
        "Stupid",
        "Lame",
        "Dumb",
    ]

    for message in messages:
        with open('test_message.txt', 'w') as f:
            f.write(message)
        result = subprocess.run(['../pre_commit_hooks/commit-msg-sentiment.py', 
                                 'test_message.txt'], capture_output=True)
        assert result.returncode == 1
        assert b'Hmmm... That was a bit negative.' in result.stdout

def test_poor_but_not_negative_commit_messages():
    messages = [
        "WIP",
        "Please work",
        "Please work!",
        "Fixed stuff",
        "Updated code",
        "Changes",
        "Refactored",
        "More changes",
        "OK, this is perfectly benign.",
        "Noice!"
    ]

    for message in messages:
        with open('test_message.txt', 'w') as f:
            f.write(message)
        result = subprocess.run(['../pre_commit_hooks/commit-msg-sentiment.py', 
                                 'test_message.txt'], capture_output=True)
        assert result.returncode == 0

        
if __name__ == '__main__':
    test_negative_commit_messages()
    test_poor_but_not_negative_commit_messages()
    print("All tests passed!")

