import a10_peter_jun as solution
import pytest
import string
from io import StringIO

@pytest.fixture
def some_text():
    return string.ascii_lowercase + '\n'

def test_write_1(some_text):
    outfile = StringIO()
    t = solution.Tee(outfile)
    t.write(some_text)

    outfile.seek(0)
    assert(outfile.read() == some_text)

def test_write_2(some_text):
    outfile1 = StringIO()
    outfile2 = StringIO()

    t = solution.Tee(outfile1, outfile2)