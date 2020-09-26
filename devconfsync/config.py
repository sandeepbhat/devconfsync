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
from logger import LOGGER


class ConfigError(Exception):
    """Custom exception class."""


class Config():
    """Provide interface for parsing and reading config file."""
    __config = dict()

    @staticmethod
    def parse(config_file: str) -> bool:
        """Parse configuration file."""
        if Config.__config:
            return True

        try:
            with open(config_file) as handle:
                Config.__config = json.load(handle)
        except FileNotFoundError:
            LOGGER.info("Error parsing config file")
            return False

        return True

    @staticmethod
    def get(key: str):
        """Get value of a given config."""
        if not Config.__config:
            raise ConfigError("Config not available!!")

        return Config.__config[key]

    @staticmethod
    def is_valid() -> bool:
        """Check if confiugration is valid or not."""
        required_keys = ["destination"]
        for key in required_keys:
            if key not in Config.__config.keys():
                return False
        return True
