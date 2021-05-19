from flask_app import app
from flask import render_template, request
from werkzeug.utils import redirect
from flask_app.models.artist import Artist
from flask_app.models.song import Songs
from flask_app.models.user import Users
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/user/dashboard')  
def userDashboard():
    return render_template("user/songDashboard.html", user = Users.get_all())

@app.route("/show/user/<userId>")
def showUser(userId):
    data = {
        "userId" : int(userId)
    }
    return render_template("clients/showUser.html", user = Users.getById(data))

@app.route("/loginReg")
def userLoginReg():
    return render_template("clients/loginReg.html")

@app.route("/process/registration", methods =["POST"])
def processRegistration():
    #todo
    return redirect(f"/show/user/{request.form['artistId']}")

@app.route('/update/user/<id>')
def editsong(id):
    return render_template('user/editUser.html', song = Users.getById(id))

@app.route("/process/update/user/<id>",methods=['POST'])
def processUserUpdate():
    Users.update(request.form)
    updatedUser= Users.getById(id)
    return redirect(f"/show/user/{updatedUser['id']}")

@app.route("/destory/user/<userId>")
def deleteSong(userId):
    data = {
        "userId" : int(userId)
    }
    Users.delete(data)
    return redirect("/artist/dashboard")