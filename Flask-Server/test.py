from models.model import User
from db import db
from flask import Flask
app = Flask(__name__)


usuario = User("steven","1234")
db.session.add(usuario)

usuarios = User.query.all()
for user in usuarios:
    print (user.username)