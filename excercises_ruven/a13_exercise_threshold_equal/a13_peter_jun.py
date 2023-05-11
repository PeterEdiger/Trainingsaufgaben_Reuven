class ThresholdEqual:
    threshold = 2

    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return abs(self.n - other.n) <= self.threshold

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __mod__(self, other):
        return self.n % other.n

    def __pow__(self, power, modulo=None):
        return self.n ** power.n

    def __str__(self):
        return str(self.n)

    def __neg__(self):
        return - self.n


# mul, truediv, mod, pow


if __name__ == "__main__":
    obj1 = ThresholdEqual(10)
    obj1.threshold = 100

    obj2 = ThresholdEqual(15)
    obj3 = ThresholdEqual(20)

    print(type(obj1 + obj2))

    print(obj1 + obj2 + obj3)

# todo dunders umschreiben, so dass man die
#  ThresholdEqual Objekte für Ausdrücke benutzen kann
