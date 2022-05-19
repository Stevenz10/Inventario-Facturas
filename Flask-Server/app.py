from flask import Flask, render_template, request, redirect, url_for
from db import db
from models.model import User
from config.config import config
app = Flask(__name__)

app.config.update(config)

@app.before_first_request
def create_db():
    db.create_all()


@app.route('/login', methods=['GET','POST'])
def Login():
    # username = request.json["username"]
    # password = request.json["password"]
    # user = User.find_by_username(username)
    # if user and password == user.password:
    #     return {"Resultado":"success"}

    # return {
    #     "Resultado":"fail",
    # }
    return render_template("login.html")

@app.route('/register', methods=['GET','POST'])
def Register():
    username = request.json["username"]
    password = request.json["password"]
    user = User(username,password)
    if User.find_by_username(username):
        return {"message": "The user already exist"}
    user.save_to_db()
    return {"message":"The user was registered succesfully"}

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)