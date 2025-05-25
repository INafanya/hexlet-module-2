class HourClock:
    def __init__(self, hour=0):
        self.hour = hour
        
    @property
    def hours(self):
        return self.hour
    
    @hours.setter
    def hours(self, new_time):
        self.hour = new_time % 12
        
        
clock = HourClock()
print(clock.hours)
clock.hours += 6
print(clock.hours)
clock.hours += 5
print(clock.hours)
    # assert clock.hours == 11
clock.hours += 4
print(clock.hours)#3
clock.hours -= 4
print(clock.hours)# 11
clock.hours = 123
print(clock.hours)# 3