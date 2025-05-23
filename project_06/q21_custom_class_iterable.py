class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 0:
            value = self.start
            self.start -= 1
            return value
        else:
            raise StopIteration

for num in Countdown(5):  # ye like a range ban gya hai 
    print(num)