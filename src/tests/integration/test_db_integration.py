import mysql.connector
from shop_app import db
from flask import g


def test_get_db(test_client, modify_db_config):
    connection = db.get_db()
    assert connection.is_connected()


def test_get_db_reconnects_disconnected_connection(test_client, modify_db_config):
    connection = db.get_db()
    connection.disconnect()

    assert not connection.is_connected()
    assert db.get_db().is_connected()


def test_already_connected_get_db(test_client, db_config):
    g.database = mysql.connector.connect(**db_config)
    assert db.get_db().is_connected()


def test_close_db(test_client, modify_db_config):
    db.get_db()
    assert isinstance(g.database, mysql.connector.connection_cext.CMySQLConnection)

    db.close_db()
    assert g.get("database") is None
