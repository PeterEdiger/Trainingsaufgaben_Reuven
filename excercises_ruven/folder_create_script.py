import os
import re

"""
This script creates a folder and file structure used in the exercises.
"""


def create_folder_name() -> (str, str):
    task_name = "counter123"  # input("What is this weeks task name?: ")
    all_folders = os.listdir()  # list of dirs

    folders = {}
    for folder in all_folders:  # regex möglich
        folder_match = re.search(r"a(\d+)_exercise", folder)
        if folder_match:
            folders[folder] = int(folder_match.group(1))

    sorted_dirs = sorted(folders.items(), key=lambda x: x[1])  # Mit dict values = Ordnernummer
    last_folder_n = sorted_dirs[-1][1]
    new_folder_n = last_folder_n + 1
    new_folder_name = f"a{new_folder_n}_exercise_{task_name}"
    return new_folder_name, new_folder_n


def create_dir_and_files():
    new_folder_name, new_folder_n = create_folder_name()
    os.makedirs(new_folder_name)  # --> Creates a dir in cwd
    excercise_text = open(f"{new_folder_name}/a{new_folder_n}_exercise_text", "w")
    excercise_text.close()
    peter_jun = open(f"{new_folder_name}/a{new_folder_n}_peter_jun.py", "w")
    peter_jun.close()
    peter_sen = open(f"{new_folder_name}/a{new_folder_n}_peter_sen.py", "w")
    peter_sen.close()
    test = open(f"{new_folder_name}/a{new_folder_n}_test.py", "w")
    test.close()
    with open(f"{new_folder_name}/a{new_folder_n}_solution_reuven.py", "w") as _f:
        _f.write("# This is test comment \n")
        _f.write("print('hello')")

        ...


if __name__ == '__main__':
    create_dir_and_files()
