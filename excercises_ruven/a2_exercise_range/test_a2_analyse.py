import a2_peter_jun as solution
import pytest

def test_myrange2_is_a_list():
    # testing if the return of function myrange2 is a list
    output = solution.myrange2(10)
    assert type(output) is list

# Explanation of Pytest - Parametrizing Tests
# https://www.tutorialspoint.com/pytest/pytest_parameterizing_tests.htm

"""Parametrizing of test is done to run the test
 against multiple sets of inputs"""

@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10,20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10,20,2))),
    (10, 20, 3, list(range(10,20,3)))
])
def test_myrange2(first, second, third, output):
    if third:
        assert solution.myrange2(first, second, third) == output
    elif second:
        assert solution.myrange2(first, second) == output
    else:
        assert solution.myrange2(first) == output
def test_myrange3_is_a_generator():
    output = solution.myrange3(10)
    assert iter(output) is output

@pytest.mark.parametrize('first, second, third, output', [
    (10, None, None, list(range(10))),
    (10, 20, None, list(range(10,20))),
    (20, 10, None, []),
    (10, 20, 2, list(range(10,20,2))),
    (10, 20, 3, list(range(10,20,3)))
])
def test_myrange3(first, second, third, output):
    if third:
        assert list(solution.myrange3(first, second, third)) == output
    elif second:
        assert list(solution.myrange3(first, second)) == output
    else:
        assert list(solution.myrange3(first)) == output