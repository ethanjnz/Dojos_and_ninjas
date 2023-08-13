from dojo_app.config.mysql_connection import connect_to_mysql

DATABASE = "dojos_and_ninjas"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
                """
        result = connect_to_mysql(DATABASE).query_db(query, form_data)
        return result
