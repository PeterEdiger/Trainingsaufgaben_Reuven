from excercises_ruven.a3_exercise_logfiles.a3_peter_jun import logtolist
import operator
from datetime import datetime


def str_to_tmsp(d):
    return datetime.strptime(d["timestamp"], "%d/%b/%Y:%H:%M:%S %z")


class LogDicts:
    def __init__(self, filename):
        file = open(filename)
        self.lst_of_dicts = logtolist(file)

    def dicts(self, key=None):
        if key:
            return sorted(self.lst_of_dicts, key=key)

        else:
            return self.lst_of_dicts

    def iterdicts(self, key=None):
        return iter(self.dicts(key))

    def earliest(self):
        sorted_list = self.dicts(key=str_to_tmsp)
        return sorted_list[0]
# Min Max benutzen bei earliest und latest.
    def latest(self):
        sorted_list = self.dicts(key=str_to_tmsp)
        return sorted_list[-1]

    def for_ip(self, ip_address, key=None):
        return [d for d in self.dicts(key) if d["ip_address"] == ip_address]

    def for_request(self, text, key=None):
        return [d for d in self.dicts(key) if text in d["request"]]


if __name__ == '__main__':

    inst = LogDicts("mini-access-log.txt")

    log_list_dicts = inst.dicts(key=None)
    for item in log_list_dicts:
        print(item)

# returns an iterator of dicts, rather than the list all at once
