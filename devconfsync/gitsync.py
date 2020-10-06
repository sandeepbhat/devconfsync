# MIT License

# Copyright (c) 2020 Sandeep Bhat

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Provide support to commit and push to git."""

from git import Repo
from logger import LOGGER


def publish_changes(destpath: str) -> bool:
    """Publish changes to remote repo."""
    repo = Repo(destpath)
    if repo.bare:
        LOGGER.info("{} is not a git repo".format(destpath))
        return False

    if not repo.is_dirty(untracked_files=True):
        LOGGER.info("No changes to publish")
        return True

    repo.git.add("--all")
    repo.git.commit("-m", "Latest developer tool settings")
    repo.git.push("origin", repo.active_branch.name)
    return True
