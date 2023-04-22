
"""
A hash file is a file that has been converted into a numerical string
by a mathematical algorithm.
"""

class DirFileHash:
    def __init__(self, folder):
        self.folder = folder

    ...

import hashlib

file_name = 'a11_mini_file'

with open(file_name) as f:
    data = f.read()

    encode = data.encode('utf-8')
    md5 = hashlib.md5(encode)
    hexdigest = md5.hexdigest()


print("----------- data -----------")
print(data)

print("----------- encode -----------")
print(encode)
print("")
print("----------- Md5 -----------")
print(md5)
print("")
print("----------- hexdigest -----------")
print(hexdigest)

"""
Was muss passieren?
Die Klasse muss files aus einem Ordner finden können. 

Falls das gesuchte file vorhanden ist.
Soll das hashvalue von diesem file returned


print(d['passwd']) 
 
"""