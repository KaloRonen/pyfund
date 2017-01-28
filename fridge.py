from contextlib import closing


class FridgeRaider:
    def open(self):
        print("open door")

    def close(self):
        print("close door")

    def take(self, food):
        print("Finding {} in fridge".format(food))
        if food == 'pizza':
            raise RuntimeError("Health warning!")
        print("Taking {} from fridge".format(food))


def raid(food):
    with closing(FridgeRaider()) as r:
        r.open()
        r.take(food)
