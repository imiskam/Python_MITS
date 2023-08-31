class Xrange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        print(f"изначальное значение value в iter: {self.value}")
        print("был вызван метод iter")
        return self

    def __next__(self):
        if self.value + self.step <= self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


example3 = Xrange(12, 24, 1)

for i in example3:
    # i = 1
    print(i)
