from flask import request, jsonify, url_for
from src.models import scenario
from src.app import app

scenario = scenario.Scenario()


# scenario views
@app.route('/scenarios', methods=['GET'])
def get_scenarios():
    return jsonify(scenario.find({})), 200


@app.route('/scenarios/<string:scenario_id>', methods=['GET'])
def get_scenario(scenario_id):
    return scenario.find_by_id(scenario_id), 200


@app.route('/scenarios', methods=['POST'])
def add_scenario():
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        steps = request.form['steps']
        response = scenario.create({'name': name, 'author': author, 'steps': steps})
        return response, 201


@app.route('/scenarios/<string:scenario_id>', methods=['PUT'])
def update_scenarios(scenario_id):
    if request.method == "PUT":
        name = request.form['name']
        author = request.form['author']
        steps = request.form['steps']
        response = scenario.create({'name': name, 'author': author, 'steps': steps})
        return response, 201


@app.route('/scenarios/<string:scenario_id>', methods=['DELETE'])
def delete_scenarios(scenario_id):
    if request.method == "DELETE":
        scenario.delete(scenario_id)
        return "Record Deleted"
