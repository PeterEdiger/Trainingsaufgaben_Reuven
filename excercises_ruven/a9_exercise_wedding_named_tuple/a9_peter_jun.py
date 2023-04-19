from collections import namedtuple, Counter, defaultdict

Person = namedtuple("Person", "first, last")


class TableFull(Exception):
    ...


class GuestList(dict):
    max_at_table = 10

    def __str__(self) -> str:
        """
        Sorts table numbers.
        Returns an organized str.
        """

        inverted_dict = defaultdict(list)
        for k, v in self.items():
            inverted_dict[v].append(k)

        sorted_table_numbers = sorted(inverted_dict, key=lambda x: 100000 if x is None else x)
        table_guests_overview = ""
        for table_number in sorted_table_numbers:
            table_guests_overview += f"{str(table_number)}\n"
            for guest in inverted_dict[table_number]:
                table_guests_overview += f"\t{guest.last}, {guest.first} \n"

        return table_guests_overview

    def assign(self, guest, table_number):
        """
        Assigns the guests to their tables.
        Checks wether the table is full.
        """
        if guest in self.keys() and table_number == self[guest]:
            return
        table_nr_free_spaces = self.free_space()
        seats_left = table_nr_free_spaces[table_number]
        if seats_left == 0:
            raise TableFull

        self[guest] = table_number

    def free_space(self) -> dict:
        """
        Checks how many free seats are available at one table.
        """
        people_on_table = Counter(self.values())
        free_spaces = {table_nr: 10 - count for table_nr, count in people_on_table.items()}
        return defaultdict(lambda: GuestList.max_at_table, free_spaces)

    def guests(self):
        guest_list = [[p, t] for p, t in self.items()]
        sorted_guest_table_list = sorted(guest_list, key=lambda x: (x[1], x[0].last, x[0].first))
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
    gl.assign(Person(last="Durr", first="Stefan"), 1)
    gl.assign(Person(last="Hoi", first="Anna"), 2)
    gl.assign(Person(last="Blast", first="Dieter"), 1)
    gl.assign(Person(last="Hein", first="Xigong"), None)

    print(gl)

# todo Falschen __str__ newline beheben
