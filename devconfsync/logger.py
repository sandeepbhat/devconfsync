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

"""Provides interface to logging."""

import logging
import constants


class Logger():
    """Helper class for logging."""
    __logger = None

    def setup(self):
        """Setup logging."""
        self.__logger = logging.getLogger(constants.DEV_CONF_SYNC_LOGGER)
        self.__logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.__logger.addHandler(console_handler)

    def info(self, msg, *args, **kwargs):
        """Info log."""
        self.__logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """Error log."""
        self.__logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """Warning log."""
        self.__logger.warning(msg, *args, **kwargs)


LOGGER = Logger()
LOGGER.setup()
