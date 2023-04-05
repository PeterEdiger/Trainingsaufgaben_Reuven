import os
from typing import Callable, Dict


def accept_txt(file_name: str, dir_path=None):
    """
    Checks if a file is a .txt file
    """
    if file_name[-4:] == ".txt":
        return "txt file"
    raise NameError("No text file")


def check_filename_len(file_name: str, dir_path=None):
    """
    checks if len of file is > 3
    """
    len_fl_name = len(file_name)
    if len_fl_name > 7:
        return len_fl_name
    raise Exception(len_fl_name)


def file_size(file_name: str, dir_path: str) -> int:
    return os.stat(f"{dir_path}/{file_name}").st_size


def file_checker(dir_path: str, func: Callable) \
        -> (Dict[str, object], Dict[str, object]):
    """
    Checks for certain properties of files.
    param func: Function that checks for different file properties.
    """
    success_dict = {}
    failure_dict = {}

    file_list = os.listdir(dir_path)
    for file in file_list:
        try:
            result = func(file, dir_path)
        except Exception as e:
            failure_dict[file] = e
        else:
            success_dict[file] = result

    return success_dict, failure_dict


if __name__ == '__main__':
    good_dict, bad_dict = file_checker('a7_test_dir', check_filename_len)
    print(good_dict, bad_dict)
