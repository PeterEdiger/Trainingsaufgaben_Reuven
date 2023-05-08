import random


class RandMemory:

    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self._history = []

    def __getattr__(self, name):  # name is not existing attribute
        if name != "get":
            print("Wrong attribute")
            return None
        rand_n = random.randint(self.lowest, self.highest)
        self._history.append(rand_n)
        return rand_n

    def history(self):
        return self._history


r = RandMemory(1, 10)

print(r.get)
print(r.get)
print(r.get)

print(r.history())