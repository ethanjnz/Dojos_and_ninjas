from dojo_app.config.mysql_connection import connect_to_mysql

DATABASE = "dojos_and_ninjas"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, form_data):
        query = """
                INSERT INTO dojos (name)
                VALUES (%(name)s)
"""
        result = connect_to_mysql(DATABASE).query_db(query, form_data)
        return result

    @classmethod
    def get_one(cls, dojo_id):
        pass

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM dojos
                """
        results = connect_to_mysql(DATABASE).query_db(query)
        dojos = []
        for dictionary in results:
            dojos.append(Dojo(dictionary))
        return dojos

    @classmethod
    def update(cls, form_data):
        pass

    @classmethod
    def delete(cls, dojo_id):
        pass
