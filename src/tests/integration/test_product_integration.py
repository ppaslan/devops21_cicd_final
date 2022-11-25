def test_get_products(test_client, modify_db_config):
    test_products = '[{"id":3,"name":"Screwdriver","price":79},{"id":2,"name":"Nail","price":99},{"id":1,"name":"Hammer","price":199}]'
    resp = test_client.get("/product/")

    assert resp.data.decode().strip() == test_products


def test_create_product_if_valid(test_client, modify_db_config):
    test_products = '[{"id":4,"name":"test-product","price":50},{"id":3,"name":"Screwdriver","price":79},{"id":2,"name":"Nail","price":99},{"id":1,"name":"Hammer","price":199}]'
    post_resp = test_client.post("/product/", json={"name": "test-product", "price": 50})
    get_resp = test_client.get("/product/")

    assert post_resp.status_code == 200
    assert post_resp.data.decode().strip() == '{"status":"ok"}'
    assert get_resp.data.decode().strip() == test_products


def test_create_product_with_invalid_data(test_client, modify_db_config):

    resp = test_client.post("/product/", json={})
    assert resp.status_code == 400
    assert resp.data.decode().strip() == '{"error":"Failed to parse json"}'


def test_useless_route(test_client, modify_db_config):
    resp = test_client.get("/product/useless")
    assert resp.data.decode().strip() == '{"message": "This message is quite useless"}'
