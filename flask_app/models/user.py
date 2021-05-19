from flask_app.config.mysqlconnection import connectToMySQL
class Users:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.user_name = data['user_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        users_from_db = connectToMySQL('songinfo').query_db(query)
        users = []
        for a in users_from_db:
            users.append(cls(a))
        return users
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,user_name,password,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(user_name)s,%(password)s,%(email)s,NOW(),NOW());"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def getById(cls,data):
        query = " SELECT * FROM users WHERE id = %(usersId)s;"
        results = connectToMySQL('songinfo').query_db(query,data)
        return cls(results[0])
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,user_name=%(user_name)s,password=%(password)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def delete(cls,data):
        query = query = "DELETE FROM users WHERE id=%(userId)s;"
        return connectToMySQL('songinfo').query_db(query,data)