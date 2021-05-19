from flask_app import app
from flask import render_template, request
from werkzeug.utils import redirect
from flask_app.models.artist import Artist
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def index():
    return render_template("clients/index.html")

@app.route('/artist/dashboard')  
def artistDashboard():
    return render_template("artists/artistDashboard.html", artists = Artist.get_all())

@app.route("/show/artist/<artistId>")
def showArtist(artistId):
    data = {
        "artistId" : int(artistId)
    }
    return render_template("artists/showArtist.html", artist = Artist.getById(data), artistSongs = Artist.getListOfSongs(data).songs)

@app.route("/create/artist")
def createArtistPage():
    return render_template("artists/newArtist.html")

@app.route("/process/create/artist", methods =["POST"])
def processArtistForm():
    newArtist = Artist.save(request.form)
    return redirect("/artist/dashboard")
@app.route('/update/artist/<id>')
def editArtist(id):
    return render_template('artists/editArtist.html', artist = Artist.getById(id))

@app.route("/process/update/<id>",methods=['POST'])
def processArtistUpdate():
    Artist.update(request.form)
    return redirect(f'/show/artist/{id}')

@app.route("/destory/artist/<artistId>")
def delete(artistId):
    data = {
        "artistId" : int(artistId)
    }
    Artist.delete(data)
    return redirect("/artist/dashboard")


