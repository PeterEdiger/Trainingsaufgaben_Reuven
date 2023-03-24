import os


task_name = input("What is this weeks task name?: ")
folders = os.listdir() # list of directory

for folder in folders:
    if folder[0] != "a":
        folders.remove(folder)

sorted_dirs = sorted(folders)

last_folder_n = sorted_dirs[-1][1]


new_folder_name = f"a{last_folder_n}_exercise_{task_name}"
# os.makedirs("a directory") --> Creates a dir in cwd
print(new_folder_name)

