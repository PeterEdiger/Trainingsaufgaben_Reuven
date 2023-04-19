class Tee:
    def __init__(self, *file_like_obj):
        self.files = file_like_obj

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return True

    def write(self, string):
        for file in self.files:
            file.write(string)

    def writelines(self, strings):
        for file in self.files:
            file.writelines(strings)

    def close(self):
        for file in self.files:
            file.close()


if __name__ == "__main__":
    import sys

    file1 = open("file1", "w")
    file2 = open("file2", "w")
    with Tee(file1, file2, sys.stdout) as t1:
        t1.write("Hello" + "\n")
        t1.writelines(["Hello", " World"])

    with Tee(file1, file2, sys.stdout) as t2:
        t2.write("Hello again")
