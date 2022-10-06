from flask import Flask,request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///simple.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from core.modules.data import data_bcg

with app.app_context():
    print("here")
    from core.modules.data import data_bcg
    db.create_all()
    db.session.commit()