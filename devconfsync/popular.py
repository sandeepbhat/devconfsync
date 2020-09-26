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

"""Helpers to identify popular tools and to get their config files."""

import os


POPULAR_TOOLS = ["vscode", "vim", "bash", "zsh", "tmux"]

POPULAR_CONFIGS = {
    "vscode": {
        "basepath": "$HOME/.config/Code/User/",
        "files": [
            "settings.json",
            "keybindings.json"
        ]
    },

    "vim":  {
        "basepath": "$HOME/",
        "files": [
            ".vimrc"
        ]
    },

    "zsh": {
        "basepath": "$HOME/",
        "files": [
            ".zshrc"
        ]
    },

    "bash": {
        "basepath": "$HOME/",
        "files": [
            ".bashrc"
        ]
    },

    "tmux": {
        "basepath": "$HOME/",
        "files": [
            ".tmux.conf"
        ]
    },
}


def get_config_list(entry: str) -> list:
    """Get a list of config files for a given popular tool."""
    basepath = POPULAR_CONFIGS[entry]["basepath"]
    if basepath.startswith("$HOME"):
        basepath = basepath.replace("$HOME", os.environ["HOME"])

    return ["{}/{}".format(basepath, f) for f in POPULAR_CONFIGS[entry]["files"]]
