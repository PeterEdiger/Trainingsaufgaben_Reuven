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

    def iterdicts(self, key=None):
        return iter(self.dicts(key=key))

    def earliest(self):
        sor = self.dicts(key=operator.itemgetter('timestamp'))
        return sor[0]

    def latest(self):
        sor = self.dicts(key=operator.itemgetter('timestamp'))
        return sor[-1]

    def filter_and_sort(self, filter_value, filter_func, sort_key):
        filtered = list(filter(lambda _d: filter_func(_d, filter_value), self.list_dicts))
        return filtered.sort(key=sort_key) if sort_key else filtered

    def for_ip(self, ip, key=None):
        return self.filter_and_sort(ip, lambda _d, _ip: _d['ip_address'] == _ip, key)

    def for_request(self, request, key=None):
        return self.filter_and_sort(request, lambda _d, _r: _r in _d['request'], key)
