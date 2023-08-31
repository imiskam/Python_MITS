class Xrange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __next__(self):
        if self.value + self.step <= self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


example = Xrange(6.4, 12.2, 1.3)
print(example.__next__())
print(example.__next__())
print(example.__next__())
print(example.__next__())
print(example.__next__())
print(example.__next__())
print(example.__next__())