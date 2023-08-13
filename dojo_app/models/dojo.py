from dojo_app.config.mysql_connection import connect_to_mysql
from dojo_app.models.ninja import Ninja

DATABASE = "dojos_and_ninjas"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

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
        query = """
                SELECT * FROM dojos 
                LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(dojos_id)s
                """
        data = {'dojos_id': dojo_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])

        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
    
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
