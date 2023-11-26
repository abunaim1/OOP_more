class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        return "engine started"

class Driver:
    def __init__(self) -> None:
        pass


# car "Has a" engine
# car "has a" driver
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()


# https://realpython.com/inheritance-composition-python/