from flask_app.config.mysqlconnection import connectToMySQL
class Songs:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.video = data['video']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM songs"
        songs_from_db = connectToMySQL('songinfo').query_db(query)
        songs = []
        for a in songs_from_db:
            songs.append(cls(a))
        return songs
    @classmethod
    def save(cls,data):
        query = "INSERT INTO songs (artist_id,title,video,created_at,updated_at) VALUES (%(artistId)s,%(title)s,%(video)s,NOW(),NOW());"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def getById(cls,data):
        query = " SELECT * FROM songs WHERE id = %(songsId)s;"
        results = connectToMySQL('songinfo').query_db(query,data)
        return cls(results[0])
    @classmethod
    def update(cls,data):
        query = "UPDATE songs SET title=%(title)s,video=%(video)s,artist_id=%(artistId)s,updated_at=NOW() WHERE id = %(id)s"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def delete(cls,data):
        query = query = "DELETE FROM songs WHERE id=%(songsId)s;"
        return connectToMySQL('songinfo').query_db(query,data)
