from pytest import fixture

from fruit_salad import Fruit
from fruit_salad import FruitSalad


@fixture
def fruit_bowl():
    return [Fruit(name="apple"), Fruit(name="banana")]


def test_friut_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)

    assert all(fruit.cubed for fruit in fruit_salad.fruits)
