import sys

f1 = open('f1.txt', 'w')
f2 = open('f2.txt', 'w')


class Tee:
    def __init__(self, *files):
        self.files = files

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def write(self, s):
        for f in self.files:
            f.write(s)

    def close(self):
        for f in self.files:
            f.close()


class W:
    def __init__(self, p):
        self.p = p
    def __enter__(self):
        self.f = open(self.p, 'w')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        print(exc_type,exc_val,exc_tb)
        return False
    def write(self,s):
        self.f.write(s)


# with Tee(f1, f2) as t:
#    t.write('Hallo')

with W('ohoho.txt') as f:
    f.write(9)
print('End')