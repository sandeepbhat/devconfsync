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

"""Configuration provider for devconfsync."""

import json
from . import logger

class ConfigParser():
    """Configuration parser class."""

    def __init__(self, config_file_name: str):
        """Init method."""
        self._config_file = config_file_name
        self._config = dict()
        self._logger = logger.get_logger()

    def parse(self) -> bool:
        """Parse configuration file."""
        try:
            with open(self._config_file) as handle:
                self._config = json.load(handle)
        except FileNotFoundError:
            self._logger.error("Error parsing config file")
            return False

        return True

    def get(self, key: str):
        """Get value of a given config."""
        return self._config[key]
