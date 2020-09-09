from flaskext.mysql import MySQL
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import re
import datetime

from sqlalchemy import Column, Date, Integer, String, create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.sql.expression import exists

engine = create_engine('mysql+pymysql://root:12345678@localhost/nickgame', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/nickgame'

db = SQLAlchemy(app)

class Nicks(db.Model):
    __tablename__ = 'nicks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1500))
    price = db.Column(db.Float)  
    status = db.Column(db.String(50))
    game_name = db.Column(db.String(100))
    game_info = db.Column(db.String(1500))
    code = db.Column(db.String(100))
    create_at = db.Column(db.String(150))
    images = db.Column(db.String(2000))
    game_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
