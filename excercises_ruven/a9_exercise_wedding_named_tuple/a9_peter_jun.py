from collections import namedtuple, Counter, defaultdict

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


class TableFull(Exception):
    ...


class GuestList(dict):
    max_at_table = 10

    def __str__(self):
        """
        Suche nach der Kleinsten tr aus dem dict --> values
        Erstmal sorted list nach Tischnummern
        """
        guest_table_str = ""
        guest_table_lst = [[g, table_nr] for g, table_nr in self.items()]
        sorted_guest_table_lst = sorted(guest_table_lst, key=lambda x: x[1])

        return "Class String"

    def assign(self, guest, table_number):
        table_nr_free_spaces = self.free_space()  # dict key:tn value:left seats
        seats_left = table_nr_free_spaces[table_number]
        if seats_left == 0:
            raise TableFull

        self[guest] = table_number

    def free_space(self) -> dict:
        people_on_table = Counter(self.values())
        free_spaces = {table_nr: 10 - count for table_nr, count in people_on_table.items()}
        return defaultdict(lambda: GuestList.max_at_table, free_spaces)

    def guests(self):
        guest_list = [[p, t] for p, t in self.items()]
        sorted_guest_table_list = sorted(guest_list, key=lambda x: (x[1], x[0].last_name, x[0].first_name))
        sorted_guest_list = [p for p, t in sorted_guest_table_list]

        return sorted_guest_list

    def table(self, table_number) -> list:
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

    def print(self):
        print(self)


if __name__ == "__main__":
    gl = GuestList()
    gl.assign(Person(last_name="Durr", first_name="Stefan"), 1)
    gl.assign(Person(last_name="Hoi", first_name="Anna"), 2)
    gl.assign(Person(last_name="Blast", first_name="Dieter"), 1)

    print(Person(last_name="Bla", first_name="Dieter"))
