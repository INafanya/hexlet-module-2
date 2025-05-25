class Counter:
    def __init__(self, value=0):
        self.value = value

    def inc(self, delta=1):
        next_value = self.value
        return Counter(next_value + delta)

    def dec(self, delta=1):
        return self.inc(-delta)


c1 = Counter()
print(c1.value) # 0

c2 = Counter(10)
print(c2.value) # 10

c3 = c2.inc()
print(c3.value) 