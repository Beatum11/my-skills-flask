import json
from Utils.error_handler import handle_errors
from bson import json_util
from flask import Blueprint, jsonify, request, abort

from Services.skills_service import SkillsService

skills_controller = Blueprint('skills', __name__, url_prefix='/skills')
ss = SkillsService()


# GET REQUESTS

@skills_controller.route("/")
@handle_errors
def get_articles():
    articles_list = ss.get_articles()
    if articles_list:
        return json.loads(json_util.dumps(articles_list))
    else:
        return jsonify({"message": "Can't find anything"})


@skills_controller.route("/<int:id>")
@handle_errors
def get_article(id):
    user = ss.get_article(id)
    if user:
        return json.loads(json_util.dumps(user))
    else:
        return jsonify({"message": "Article not found"})


# POST REQUESTS
@skills_controller.route("/", methods=["POST"])
@handle_errors
def create_article():
    new_article = request.get_json()
    if new_article:
        ss.add_article(new_article)
        return jsonify({"message": "Article has been added!"})
    else:
        return abort(404, "Article not found")


# PUT REQUEST
@skills_controller.route("/<int:id>", methods=["PUT"])
def update_article(id):
    updated_article = request.get_json()
    if updated_article:
        ss.update_article(id, updated_article)
        return jsonify({"message": "Article has been updated"})
    else:
        return abort(404, "Article not found")


# DELETE REQUEST
@skills_controller.route("/<int:id>", methods=["DELETE"])
def delete_article(id):
    ss.delete_article(id)
    return jsonify({"message": "DONE"}), 200
