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

"""Main entry for devconfsync."""

import pathlib
import distutils.dir_util as dir_util
import distutils.file_util as file_util
import argparse
import sys
import popular
import gitsync
from logger import LOGGER
from config import Config


def parse_cmdline_opts():
    """Parse command line options."""
    parser = argparse.ArgumentParser(
        description="devconfsync - Sync your development tool settings")
    parser.add_argument(
        "-c", "--config", dest="config", required=True, help="devconfsync JSON configuration file")
    return parser.parse_args()


def copy_files(file_list: list, dest_dir: str) -> bool:
    """Copy the given list of files to specified destination dir."""
    if not pathlib.Path(dest_dir).exists():
        LOGGER.error("Destination dir does not exist")
        return False

    for file in file_list:
        LOGGER.info("Copying {} -> {}".format(file, dest_dir))
        if pathlib.Path(file).is_dir():
            dir_util.copy_tree(file, dest_dir)
        else:
            file_util.copy_file(file, dest_dir)

    return True


def create_dir(dir_name: str, destination: str):
    """Create dirs at the destination given a list of names."""
    if not pathlib.Path(destination).exists():
        LOGGER.error("Destination dir does not exist")
        return False

    LOGGER.info("Creating dir -> {}".format(dir_name))
    pathlib.Path("{}/{}".format(destination, dir_name)).mkdir(exist_ok=True)
    return True


if __name__ == "__main__":
    options = parse_cmdline_opts()

    if not Config.parse(options.config):
        LOGGER.error("Error parsing configuraion")
        sys.exit(-1)

    if not Config.is_valid():
        LOGGER.error("Invalid configuration")
        sys.exit(-1)

    dest_git_dir = Config.get("destination")
    if not pathlib.Path(dest_git_dir).exists():
        LOGGER.error("Destination git dir does not exist")
        sys.exit(-1)

    # Get config files for popular tools
    tools = Config.get("tools")
    if tools:
        for tool in tools:
            if tool in popular.POPULAR_TOOLS:
                # Create a dir with name of the tool at destination
                create_dir(tool, dest_git_dir)
                # Get the list of config files for the tool
                popular_configs = popular.get_config_list(tool)
                # Copy the files
                copy_files(popular_configs, "{}/{}".format(dest_git_dir, tool))
            else:
                LOGGER.error("{} tool not recognized: consider using \"files\" section")

    # Get user defined file list
    userdefined_files = Config.get("files")
    # Copy user defined files
    if userdefined_files:
        copy_files(userdefined_files, dest_git_dir)

    gitsync.publish_changes(dest_git_dir)
