class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad():
    def __init__(self, *fruit_bowl) -> None:
        self.fruits = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruits:
            fruit.cube()
