from excercises_ruven.a3_exercise_logfiles.a3_peter_jun import logtolist

"""Ich brauche eine Klasse die bei einer Instanziierung" \
die bereits gebaute Funktion benutzt um ein list of dicts zu benutzen.


"""


class LogDicts():
    def __init__(self, filename):
        file = open(filename)
        self.lst_of_dicts = logtolist(file)



    def dicts(self, key=None):
        if key == "by_ip_address":
            return sorted(self.lst_of_dicts, key=lambda i: i["ip_address"])

        else:
            return self.lst_of_dicts

    def iterdicts(self):
        return iter(self.lst_of_dicts)



inst = LogDicts("mini-access-log.txt")

log_list_dicts = inst.dicts(key="by_ip_address")
for item in log_list_dicts:
    print(item)

# returns an iterator of dicts, rather than the list all at once
