from excercises_ruven.a3_exercise_logfiles.a3_peter_jun import logtolist
import operator



class LogDicts():
    def __init__(self, filename):
        file = open(filename)
        self.lst_of_dicts = logtolist(file)

    def dicts(self, key=None):
        if key:
            return sorted(self.lst_of_dicts, key=key)

        else:
            return self.lst_of_dicts

    def iterdicts(self):
        return iter(self.lst_of_dicts)


if __name__ == '__main__':

    inst = LogDicts("mini-access-log.txt")

    log_list_dicts = inst.dicts(key=operator.itemgetter('ip_address'))
    for item in log_list_dicts:
        print(item)

# returns an iterator of dicts, rather than the list all at once
