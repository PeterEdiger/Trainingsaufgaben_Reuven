from a9_peter_jun import GuestList, Person  # , TableFull
import pytest


@pytest.fixture
# List of named tuples namedtuple("Person", "first_name, last_name")
def some_people():
    return [Person('Waylon', 'Dalton'),
            Person('Justine', 'Henderson'),
            Person('Abdullah', 'Lang'),
            Person('Marcus', 'Cruz'),
            Person('Thalia', 'Cobb'),
            Person('Mathias', 'Little'),
            Person('Eddie', 'Randolph'),
            Person('Angela', 'Walker'),
            Person('Lia', 'Shelton'),
            Person('Hadassah', 'Hartman'),
            Person('Joanna', 'Shaffer'),
            Person('Jonathon', 'Sheppard')]


@pytest.fixture
# Populates the and adds table number
def populated_tables(some_people) -> object:
    gl = GuestList()
    for table_number, one_person in enumerate(some_people):
        gl.assign(one_person, table_number)
    return gl


def test_empty_table():
    gl = GuestList()
    assert len(gl) == 0
    assert gl.free_space() == {}


def test_with_a_few_people(some_people):
    gl = GuestList()
    # assigning None to table 0
    for table_number, one_person in enumerate(some_people[:5]):
        if table_number == 0:
            gl.assign(one_person, None)
        else:
            gl.assign(one_person, table_number)

    assert len(gl) == 5
    # test if one table fits unassigned logic
    assert len(gl.unassigned()) == 1
    # Which person is unnasigned
    assert gl.unassigned() == [some_people[0]]
    for table_number in range(1, 5):
        # checks if method table returns the right people
        assert gl.table(table_number) == [some_people[table_number]]


def test_get_guests(some_people, populated_tables):
    # The tables get populated with my logic
    gl = populated_tables

# {Person(first_name='Waylon', last_name='Dalton'): 0, Person(first_name='Justine', last_name='Henderson'): 1, Person(first_name='Abdullah', last_name='Lang'): 2, Person(first_name='Marcus', last_name='Cruz'): 3, Person(first_name='Thalia', last_name='Cobb'): 4, Person(first_name='Mathias', last_name='Little'): 5, Person(first_name='Eddie', last_name='Randolph'): 6, Person(first_name='Angela', last_name='Walker'): 7, Person(first_name='Lia', last_name='Shelton'): 8, Person(first_name='Hadassah', last_name='Hartman'): 9, Person(first_name='Joanna', last_name='Shaffer'): 10, Person(first_name='Jonathon', last_name='Sheppard'): 11}

    assert gl.guests() == some_people

def test_table_full(some_people):
    gl = GuestList()
    for one_person in some_people[:GuestList.max_at_table]:
        gl.assign(one_person, 1)
    assert len(gl) == GuestList.max_at_table
    with pytest.raises(TableFull):
        gl.assign(some_people[GuestList.max_at_table], 1)


def test_table_free_space(some_people):
    gl = GuestList()
    for one_person in some_people[:GuestList.max_at_table - 1]:
        gl.assign(one_person, 1)
    assert (gl.free_space()) == {1: 1}

    gl.assign(one_person, 2)
    assert (gl.free_space()) == {1: 2, 2: GuestList.max_at_table - 1}


def test_repr(some_people):
    gl = GuestList()
    assigned_people = some_people[:GuestList.max_at_table]
    for one_person in assigned_people:
        gl.assign(one_person, 1)

    output = str(gl)
    assert output.startswith('1\n')
    for one_person in assigned_people:
        assert f'{one_person.last}, {one_person.first}' in output
