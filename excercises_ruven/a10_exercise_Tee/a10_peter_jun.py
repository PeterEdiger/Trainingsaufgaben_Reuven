class Tee:
    def __init__(self, *file_like_obj):
        self.files = file_like_obj

    def __entry__(self):
        ...

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
    t1 = Tee(file1, file2, sys.stdout)

    t1.write("Hello" + "\n")
    t1.writelines(["Hello", " World"])
    t1.close()
