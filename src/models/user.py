from src.factory.validation import Validator
from src.factory.database import Database


class User(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = 'users'  # collection name

        self.fields = {
            "login": "string",
            "fullname": "string"
        }

        self.create_required_fields = ["login", "fullname"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = ["fullname"]

        # Fields optional for UPDATE
        self.update_optional_fields = ["login"]

    def create(self, user):
        # Validator will throw error if invalid
        self.validator.validate(user, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(user, self.collection_name)
        return "Inserted Id " + res

    def find(self, user):  # find all
        return self.db.find(user, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, user):
        self.validator.validate(user, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, user, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
