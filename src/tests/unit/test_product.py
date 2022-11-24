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
