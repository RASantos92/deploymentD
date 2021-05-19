from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.song import Songs
class Artist:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.hometown = data['hometown']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.songs = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM artist"
        artist_from_db = connectToMySQL('songinfo').query_db(query)
        artist = []
        for a in artist_from_db:
            artist.append(cls(a))
        return artist
    @classmethod
    def save(cls,data):
        query = "INSERT INTO artist (name,hometown,created_at,updated_at) VALUES (%(name)s,%(hometown)s,NOW(),NOW());"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def getById(cls,data):
        query = " SELECT * FROM artist WHERE id = %(artistId)s;"
        results = connectToMySQL('songinfo').query_db(query,data)
        return cls(results[0])
    @classmethod
    def update(cls,data):
        query = "UPDATE artist SET name=%(name)s,hometown=%(hometown)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def delete(cls,data):
        query = query = "DELETE FROM artist WHERE id=%(artistId)s;"
        return connectToMySQL('songinfo').query_db(query,data)
    @classmethod
    def getListOfSongs(cls,db):
        query = "SELECT * FROM songs JOIN artist ON artist.id = songs.artist_id WHERE artist.id = %(artistId)s;"
        results = connectToMySQL('songinfo').query_db(query,db)
        songList = cls(results[0])
        for row_from_db in results:
            data={
                "id": row_from_db['artist_id'],
                "title": row_from_db['title'],
                "video": row_from_db['video'],
                "created_at": row_from_db['created_at'],
                "updated_at": row_from_db['updated_at'],
            }
            songList.songs.append(Songs(data))
        return songList


