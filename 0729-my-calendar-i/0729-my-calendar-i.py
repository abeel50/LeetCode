class MyCalendar:

    def __init__(self):
        self.bookings = OrderedDict()
        
    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings.keys():
            if max(s, start) < min(e, end):
                return False
        self.bookings[(start, end)] = True
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)