import os.path
import hashlib


class DirFileHash(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, filename):
        # os.path.join() concatenates the args with added
        # / <dirname/filename>
        fullname = os.path.join(self.dirname, filename)
        if os.path.exists(fullname) and os.path.isfile(fullname):
            m = hashlib.md5()
            m.update(open(fullname, 'rb').read())
            return m.hexdigest()


class DirFileHash1(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, filename):
        # os.path.join() concatenates the args with added
        # / <dirname/filename>
        fullname = os.path.join(self.dirname, filename)
        if os.path.exists(fullname) and os.path.isfile(fullname):
            m = hashlib.md5()
            with open(fullname, "rb") as f:
                for line in f:
                    m.update(line)
            return m.hexdigest()


if __name__ == "__main__":
    instance = DirFileHash("a11_test_directory")
    instance1 = DirFileHash1("a11_test_directory")
    print(instance["a11_mini_file"])
    print(instance1["a11_mini_file"])