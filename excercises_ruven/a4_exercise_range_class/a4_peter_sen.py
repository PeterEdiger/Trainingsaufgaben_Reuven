from excercises_ruven.a3_exercise_logfiles.a3_peter_sen import re_logtolist
import operator


class LogDicts:
    def __init__(self, file_name):
        with open(file_name) as file:
            self.list_dicts = re_logtolist(file)

    def dicts(self, key=None):
        if key:
            return sorted(self.list_dicts, key=key)
        return self.list_dicts

    def iterdicts(self,key=None):
        return iter(self.dicts(key=key))

    def earliest(self):
        sor = self.dicts(key=operator.itemgetter('timestamp'))
        return sor[0]

    def latest(self):
        sor = self.dicts(key=operator.itemgetter('timestamp'))
        return sor[-1]

    def for_ip(self, ip,key=None):
        return [d for d in self.dicts(key) if d['ip_address'] == ip]

    def for_request(self, request,key=None):
        return [d for d in self.dicts(key) if request in d['request']]
