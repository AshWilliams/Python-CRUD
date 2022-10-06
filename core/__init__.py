from flask import Flask,request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///simple.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
