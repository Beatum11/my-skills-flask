from functools import wraps
from pymongo.errors import ServerSelectionTimeoutError, PyMongoError
from flask import jsonify


def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ServerSelectionTimeoutError:
            return jsonify({"error": "Database connection failed"}), 500
        except PyMongoError as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return decorated_function
