# # from flask import g
# import pytest
# import mysql.connector
# import os
# from shop_app import create_app
# from shop_app import db


# def is_responsive(config):
#     try:
#         conn = mysql.connector.connect(**config)
#         return conn.is_connected()
#     except Exception:
#         return False


# @pytest.fixture(scope="session")
# def docker_compose_file(pytestconfig):
#     return os.path.join(str(pytestconfig.rootdir), "tests", "integration", "docker-compose.yml")


# @pytest.fixture(scope="session")
# def db_config(docker_ip, docker_services):
#     """Ensure that HTTP service is up and responsive."""

#     docker_port = docker_services.port_for("db", 3306)
#     config = {
#         "host": docker_ip,
#         "user": "shopapp",
#         "password": "thisisfortest",
#         "port": docker_port,
#         "database": "shopapp",
#     }

#     docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=lambda: is_responsive(config))
#     return config


# @pytest.fixture()
# def test_client():
#     app = create_app()
#     with app.test_client() as test_client:
#         with app.app_context():
#             yield test_client


# @pytest.fixture()
# def modify_db_config(mocker, db_config):
#     yield mocker.patch("shop_app.db.get_db_config", return_value=db_config)


# def test_something(test_client, modify_db_config):
#     z = test_client.get("/")
#     assert z.data == "d"
