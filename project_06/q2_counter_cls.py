class Counter:

    Total_Count = 0

    def __init__(self):
        Counter.Total_Count += 1

    @classmethod
    def displayCount(cls):
        print(f"You created total {cls.Total_Count} objects.🙌")
    
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()
c6 = Counter()

Counter.displayCount()