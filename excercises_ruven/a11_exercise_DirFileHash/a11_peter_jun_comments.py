import hashlib, os


class DirFileHash:
    """
    Every instance of this class gets a folder_path property.

    """
    def __init__(self, folder_path):
        self.folder = folder_path
        all_files = os.listdir(folder_path)
        # filter for only files in the directory
        only_files = list(filter(lambda x: os.path.isfile(folder_path + "/" + x), all_files))
        print(only_files)

        self.only_files_dict = {file_name: hashing(folder_path, file_name) for file_name in only_files}
        print(self.only_files_dict)

    def __getitem__(self, file_name):
        if file_name in self.only_files_dict:
            return self.only_files_dict[file_name]
        else:
            return None


def hashing(folder_path, file_name):
    """
    This function is hashing a file.

    """
    with open(folder_path + "/" + file_name) as f:
        data = f.read()

        encode = data.encode('utf-8')
        md5 = hashlib.md5(encode)
        hexdigest = md5.hexdigest()
        return hexdigest


if __name__ == "__main__":
    test_1 = DirFileHash("a11_test_directory")

    print(test_1["a11_mini_file"])
