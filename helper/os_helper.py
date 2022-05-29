# -*- coding: utf-8 -*-

# --- Python modules ---
# os: library that allows access to functionalities dependent on the Operating System.
from os import path
# sys: module which provides access to variables used or maintained by the interpreter and to functions that
#      interact strongly with the interpreter
import sys

# --- App modules ---
from . import string_helper


def file_exists(filename_: str,
                *sub_folders) -> ():
    """
    Evaluates if file exists in the path app_folder/<*sub_folders>/filename
    :param filename_: to evaluate existence
    :param sub_folders: dependent on the application folder
    :return: a tuple (True whether filename exists, otherwise False,
                      Full path)
    """

    # Check filename has a value, if it does not, reject
    if string_helper.is_none_empty_space(filename_):
        return False, None

    # Identify the application directory
    app_folder_ = path.abspath(path.dirname(str(sys.modules['__main__'].__file__)))
    # Get path with sub-folders (app_folder/<*sub_folders>)
    file_folder_ = path.join(app_folder_, *sub_folders)
    # Get full path with filename (app_folder/<*sub_folders>/filename)
    full_file_path_ = path.join(file_folder_, filename_)

    # Evaluate file existence, and return result
    return path.exists(full_file_path_), full_file_path_
