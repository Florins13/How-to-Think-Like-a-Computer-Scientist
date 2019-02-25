# Ex 1
from unit_tester import test


class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # Ex 2
    def between(self, t1, t2):
        t1seconds = t1.to_seconds()
        t2seconds = t2.to_seconds()
        myseconds = self.to_seconds()
        if t1seconds <= myseconds < t2seconds:
            return True
        return False

    # Ex 3
    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    # Ex 4
    def increment(self, seconds):
        # print(self.to_seconds())
        totalsecs = self.to_seconds() + seconds
        if totalsecs < 0:
            print("You are trying to substract to much")
            return self.to_seconds
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60


# def between(t1, t2, t3):
#     hour = t1.hours + t2.hours
#     minutes = t1.minutes + t2.minutes
#     seconds = t1.seconds + t2.seconds
#     if t1.hours <= time3.hours < t2.hours:
#         if t1.minutes <= time3.minutes < t2.minutes:
#             if t1.seconds <= time3.seconds < t2.seconds:
#                 return True
#     return False


def between(t1, t2, s):
    t1seconds = t1.to_seconds()
    t2seconds = t2.to_seconds()
    Aseconds = s.to_seconds()
    if t1seconds <= Aseconds < t2seconds:
        return True
    return False


time1 = MyTime(1, 1, 1)
time2 = MyTime(10, 10, 10)
time3 = MyTime(5, 5, 5)
t3 = time2 > time1
print(t3)


# Ex 5

time2.increment(-120)
test((time2.minutes) == 8)
time2.increment(120)
test((time2.minutes) == 10)
time2.increment(-36610)  # All the time in seconds
test((time2.hours) == 0)
time2.increment(-36611)  # Here we are trying to substract with 1 second more.
test((time2.hours) == time2.to_seconds())

# print(between(time1, time2, time3))
# print(time3.between(time1, time2))
