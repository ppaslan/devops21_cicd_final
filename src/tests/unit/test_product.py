from shop_app import product


def test_include_column_names():
    resultset = [(3, "Screwdriver", 79), (2, "Nail", 99), (1, "Hammer", 199)]
    description = [
        ("id", 3, None, None, None, None, 0, 49667, 63),
        ("name", 253, None, None, None, None, 1, 0, 255),
        ("price", 3, None, None, None, None, 1, 32768, 63),
    ]
    column_names = product.include_column_names(resultset, description)

    assert column_names == [
        {"id": 3, "name": "Screwdriver", "price": 79},
        {"id": 2, "name": "Nail", "price": 99},
        {"id": 1, "name": "Hammer", "price": 199},
    ]


def test_increase_by_one():
    value = product.increase_by_one(1)
    assert value == 2


def test_useless_message():
    message = product.useless_message()
    assert message == {"message": "This message is quite useless"}

def test_return_my_name():
    my_name = product.return_my_name()
    assert my_name == {"name": "My name is Zoro"}