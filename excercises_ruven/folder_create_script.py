import os
import re

"""
This script creates a folder and file structure used in the exercises.
"""

my_task_name = "threshold_decorator"

def create_folder_name(task_name) -> (str, str):
    all_folders = os.listdir()  # list of dirs

    folders = {}
    for folder in all_folders:
        folder_match = re.search(r"a(\d+)_exercise", folder)
        if folder_match:
            folders[folder] = int(folder_match.group(1))

    # Sorts folders items by value. The value is the folder number
    sorted_dirs = sorted(folders.items(), key=lambda x: x[1])  # Mit dict values = Ordnernummer
    highest_folder_number = sorted_dirs[-1][1]
    new_folder_n = highest_folder_number + 1
    new_folder_name = f"a{new_folder_n}_exercise_{task_name}"
    return new_folder_name, new_folder_n


def create_dir_and_files(task_name):

    new_folder_name, new_folder_n = create_folder_name(task_name)
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
    create_dir_and_files(my_task_name)
