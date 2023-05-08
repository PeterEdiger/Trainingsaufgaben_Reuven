import os.path
import hashlib


class DirFileHash(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, filename):
        # os.path.join() concatenates the args with added "/"
        #  <dirname/filename>
        fullname = os.path.join(self.dirname, filename)
        if os.path.exists(fullname) and os.path.isfile(fullname):
            m = hashlib.md5()
            m.update(open(fullname, 'rb').read())
            return m.hexdigest()
