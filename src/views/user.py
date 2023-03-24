from flask import request, jsonify, url_for
from src.models import user
from src.app import app

user = user.User()


# user views
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user.find({})), 200


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    return user.find_by_id(user_id), 200


@app.route('/users', methods=['POST'])
def add_users():
    if request.method == "POST":
        login = request.form['login']
        fullname = request.form['fullname']
        response = user.create({'login': login, 'fullname': fullname})
        return response, 201


@app.route('/users/<string:user_id>', methods=['PUT'])
def update_users(user_id):
    if request.method == "PUT":
        login = request.form['login']
        fullname = request.form['fullname']
        response = user.update(user_id, {'login': login, 'fullname': fullname})
        return response, 201


@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_users(user_id):
    if request.method == "DELETE":
        user.delete(user_id)
        return "Record Deleted"
