from __future__ import annotations

from setuptools import setup


setup(
    name='pre_commit_placeholder_package',
    version='0.0.0',
    install_requires=['textblob', 'afinn'],
    scripts=['pre_commit_hooks/commit-message-sentiment.py']
)
