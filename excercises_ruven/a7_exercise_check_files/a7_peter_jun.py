"""
I need a function that takes
two parameters --> directory_path and a function

The function should return 2 dicts.

# Dict One:
key          value:
filenames    certain file properties

Dict Two:
key          value:
filename     exceptions if raised
"""
import os
from typing import Callable, Dict


def accept_txt(file_name:str, dir_name = None):
    if file_name[-4:] == ".txt":
        return "txt file"
    raise NameError("No text file")

def funcfile(file_name:str, dir_name = None)->str:
    if len(file_name) > 3:
        return "Its longer 3"
    else:
        return "Its not longer than 3"

def file_size(file_name:str, dir_path:str)->int:
    return os.stat(f"{dir_path}/{file_name}").st_size



def file_checker(dir_path: str, func: Callable[[str],object])\
        -> (Dict[str, object], Dict[str, object]):

    success_dict = {}
    except_dict = {}

    file_list = os.listdir(dir_path)
    for file in file_list:
        try:
            result = func(file, dir_path)
        except Exception as e:
            except_dict[file] = e
        else:
            success_dict[file] = result

    return success_dict, except_dict


if __name__ == '__main__':
    good_dict, bad_dict = file_checker('a7_test_dir', file_size)
    print(good_dict, bad_dict)

# todo: Die Logik soll unterscheiden ob es ein file_name oder file_path ist.
# todo: Interface zwischen Funktionen klar defenieren.
"""
Currently func(file_name) # Bad because we can not analyze files. 
Three possibilities:
1: func(file_path: str)
2: func(dir_path: str, file_name: str)
3: func(file: fileobject)
    
"""