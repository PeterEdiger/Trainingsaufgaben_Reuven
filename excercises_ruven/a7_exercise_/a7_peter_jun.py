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




def file_checker(dir_path: str, func) -> (dict, dict):
    """
    Getting list of files from dir_path
    success_dict = {}
    exception_dict = {}
    Iterate through files in dir
        Try check for file property.
            If success:
                populate success dict
            If not success:
                populate exception dict.
     return success_dict, exception_dict


    """
    ...


print(type(file_checker))
