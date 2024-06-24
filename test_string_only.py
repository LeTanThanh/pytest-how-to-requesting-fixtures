from pytest import fixture


@fixture
def first_entry():
    return "a"


@fixture
def order():
    return []


@fixture
def append_first(order, first_entry):
    print("append_first")
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    assert order == [first_entry]
