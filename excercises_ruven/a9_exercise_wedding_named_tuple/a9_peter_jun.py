from collections import namedtuple, Counter

"""
Was muss method assign können. 

Diese Methode muss in der Lage sein Menschen hinzuzufügen. 
Spezieller gesagt soll sie namedtuples entgegennehmen.

Was kann eine named tuple?



Wir arbeiten mit nur einem Object. 
Dieses Object muss in der Lage sein immer weitere Personen aufzunehmen. 


gl = GuestList()

### gl.assingn bekommt einen Parameter 
### dieser ist eine named tuple mit dem Namen Person und 
### einer tuple (first_name, last_name) der zweite Parameter ist die Table Nummer. 
gl.assign(Person('Waylon', 'Dalton'), 1)
"""

Person = namedtuple("Person", "first_name, last_name")

p_2 = Person("Rudi", "Völler")

"""
Was ist das Problem?
Wenn ein Gast zum zweiten mal assigned werden soll.
Soll er einen neuen Tisch zugewiesen bekommen. 

Iterieren durch bestehen Liste
Abgleichen ob guest bereits vorhanden ist. 
Wenn nicht append.()
Wenn ja update. mit neuem Table 
"""


class GuestList(dict):

    def assign(self, guest, table_number):

        self[guest] = table_number
        already_on_table = Counter(self.values())
        for table_count in already_on_table.values():
            if table_count < 10:
                continue
            raise Exception 

    def free_space(self):
        table_numbers = []
        for table_number in self.values():
            table_numbers.append(table_number)
        people_on_table = Counter(table_numbers)
        left_seats = {}
        for count_tuple in people_on_table.items():
            left_seats[count_tuple[1]] = 10 - count_tuple[0]
        return left_seats

    def table(self, table_number):
        persons = []

        for person, tbl_nr in self.items():
            if tbl_nr == table_number:
                persons.append(person)
        return persons

    def unassigned(self):
        persons = []
        for person, tbl_nr in self.items():
            if tbl_nr is None:
                persons.append(person)
        return persons


gl = GuestList()
gl.assign(Person('Waylon', 'Dalton'), 1)
print(len(gl))
gl.assign(Person('Waylon', 'Dalton'), 2)
print(len(gl))
gl.assign(Person('Stefan', 'Dalton'), 2)
print(len(gl))

gl.free_space()

print(gl.table(2))
