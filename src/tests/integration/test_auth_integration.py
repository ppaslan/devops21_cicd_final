import pytest
from flask import session


def test_register_user(test_client, modify_db_config):
    resp = test_client.post("/auth/register", data={"username": "testuser", "password": "testuser"})
    assert resp.status_code == 302


def test_register_already_existing_user(test_client, modify_db_config):
    error_msg = "User testuser is already registered"
    resp = test_client.post("/auth/register", data={"username": "testuser", "password": "testuser"})

    assert error_msg in resp.data.decode()

def test_register_without_username_or_pass(test_client, modify_db_config):
    username_error = "Username is required."
    password_error = "Password is required."

    user_resp = test_client.post("/auth/register", data={"username": "", "password": "testuser"})
    pass_resp = test_client.post("/auth/register", data={"username": "testuser", "password": ""})

    assert username_error in user_resp.data.decode()
    assert password_error in pass_resp.data.decode()

def test_login_wrong_credentials(test_client, modify_db_config):
    username_error = "Incorrect username."
    password_error = "Incorrect password."

    user_resp = test_client.post("/auth/login", data={"username": "does not exist", "password": "testuser"})
    pass_resp = test_client.post("/auth/login", data={"username": "testuser", "password": "wrong pass"})

    assert username_error in user_resp.data.decode()
    assert password_error in pass_resp.data.decode()


def test_login(test_client, modify_db_config):
    test_client.post("/auth/login", data={"username": "testuser", "password": "testuser"}, follow_redirects=True)
    assert session["user_id"] == 1

def test_logout(test_client, modify_db_config):
    assert session["user_id"] == 1
    resp = test_client.get("/auth/logout", follow_redirects=True)

    with pytest.raises(KeyError):
        assert session["user_id"] == 1

    assert len(resp.history) == 1
    assert resp.request.path == "/"
