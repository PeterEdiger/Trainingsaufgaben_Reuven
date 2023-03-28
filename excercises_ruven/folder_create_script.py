import os
import re

"""
This script creates a folder and file structure used in the exercises.
"""


def create_folder_name(task_name) -> (str, str):
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
    new_folder_name, new_folder_n = create_folder_name("multizeperator")
    os.makedirs(new_folder_name)  # --> Creates a dir in cwd
    file_names = [
        "exercise_text", "peter_jun.py",
        "peter_sen.py", "test.py",
        "solution_reuven.py",
    ]
    for _fl in file_names:
        with open(f"{new_folder_name}/a{new_folder_n}_{_fl}", "w"):
            ...


if __name__ == '__main__':
    create_dir_and_files()
