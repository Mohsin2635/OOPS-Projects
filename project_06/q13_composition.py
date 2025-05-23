class Engine:
    def start_engine(self):
        print("Rikshaw Engine Started🛺")

class Rikshaw:
    def __init__(self, engine_object):
        self.engine_object = engine_object

    def start_rikshaw(self):
        self.engine_object.start_engine()

rikshaw_engine = Engine()

my_rikshaw = Rikshaw(rikshaw_engine)

my_rikshaw.start_rikshaw()
