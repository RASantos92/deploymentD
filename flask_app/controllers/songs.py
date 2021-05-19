from flask_app import app
from flask import render_template, request
from werkzeug.utils import redirect
from flask_app.models.artist import Artist
from flask_app.models.song import Songs
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/song/dashboard')  
def songDashboard():
    return render_template("songs/songDashboard.html", songs = Songs.get_all())

@app.route("/show/song/<songId>")
def showSong(songId):
    data = {
        "songId" : int(songId)
    }
    return render_template("songs/showSong.html", song = Songs.getById(data))

@app.route("/create/song")
def createSongPage():
    return render_template("songs/newSong.html")

@app.route("/process/create/song", methods =["POST"])
def processSongForm():
    newSong = Songs.save(request.form)
    return redirect(f"/show/artist/{request.form['artistId']}")
@app.route('/update/song/<id>')
def editsong(id):
    return render_template('songs/editSong.html', song = Songs.getById(id))

@app.route("/process/update/<id>",methods=['POST'])
def processSongUpdate():
    Songs.update(request.form)
    updatedSong = Songs.getById(id)
    return redirect(f"/show/song/{updatedSong['id']}")

@app.route("/destory/song/<songId>")
def deleteSong(songId):
    data = {
        "songId" : int(songId)
    }
    Songs.delete(data)
    return redirect("/artist/dashboard")