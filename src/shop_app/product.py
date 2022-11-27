from flask import Blueprint, jsonify, request
from shop_app.db import get_db

bp = Blueprint("product", __name__, url_prefix="/product")


def include_column_names(resultset, description):
    """Include needed colum names"""

    column_names = [row[0] for row in description]
    return [dict(zip(column_names, row)) for row in resultset]


@bp.route("/")
def index():
    """Show all the products"""
    with get_db().cursor() as cur:
        cur.execute("SELECT * from products" " ORDER BY name DESC")
        products = cur.fetchall()
        return jsonify(include_column_names(products, cur.description))


@bp.route("/useless")
def useless_route():
    """Useless"""
    return jsonify(useless_message())

@bp.route("/my_name")
def my_name_route():
    """My name"""
    return jsonify(return_my_name())


@bp.route("/", methods=("POST",))
def create_product():
    """Add a product"""
    json_payload = request.get_json()
    if json_payload:
        database = get_db()
        with database.cursor(prepared=True) as cur:
            stmt = "INSERT INTO products(name, price) VALUES (%s, %s)"
            cur.execute(stmt, (json_payload["name"], int(json_payload["price"])))
            database.commit()
            return jsonify({"status": "ok"})
    return jsonify({"error": "Failed to parse json"}), 400


def increase_by_one(number):
    return number + 1


def useless_message():
    return {"message": "This message is quite useless"}

def return_my_name():
    return {"name": "My name is Zoro"}
