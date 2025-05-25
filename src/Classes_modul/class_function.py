class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta
        return self.value

    def dec(self, delta=1):
        self.value -= delta
        if self.value > 0:
            return self.value
        else:
            return 0
# Ршение учителя
class Counter_teacher:
    value = 0

    def inc(self, delta=1):
        next_value = self.value + delta
        self.value = next_value

    def dec(self, delta=1):
        self.inc(-delta)
    
c = Counter_teacher()
c.inc()
c.inc()
print(c.value)
c.inc(40)
print(c.value)  # 42
c.dec()
c.dec(30)
print(c.value)  # 11
