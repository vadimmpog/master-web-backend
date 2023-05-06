from src.factory.database import Database
from src.factory.validation import Validator


class Scenario(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = 'scenarios'  # collection name

        self.fields = {
            "author": "string",
            "name": "string",
            "steps": "lst"
        }

        self.create_required_fields = ["author", "name", "steps"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = []

        # Fields optional for UPDATE
        self.update_optional_fields = []

    def create(self, scenario):
        # Validator will throw error if invalid
        self.validator.validate(scenario, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(scenario, self.collection_name)
        return "Inserted Id " + res

    def find(self, scenario):  # find all
        return self.db.find(scenario, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, scenario):
        self.validator.validate(scenario, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, scenario, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
