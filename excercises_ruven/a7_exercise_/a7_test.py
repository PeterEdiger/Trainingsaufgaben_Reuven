from a7_peter_jun import file_checker
import os

def check_file(file):
    return "a"
def always_raise(file):
    raise ValueError

def test1():
    success_dict, exepction_dict =  file_checker('a7_test_dir', check_file)
    assert type(success_dict) == dict
    assert len(success_dict) == 3
    for filename in success_dict:
        assert success_dict[filename] == "a"
    assert len(exepction_dict) == 0