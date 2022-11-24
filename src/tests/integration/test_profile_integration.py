from flask import render_template

def test_profile_root(test_client, modify_db_config):
    resp = test_client.get("/")
    assert resp.data.decode() == render_template("profile.html")
