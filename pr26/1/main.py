from flask import Flask, request
from flask import render_template
from datetime import datetime

import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Admin(db.Model):
    __tablename__ = 'Administrator_data'
    id = db.Column(db.Integer(), primary_key=True)
    admin_login = db.Column(db.String(30), nullable = False, unique = True)
    admin_password = db.Column(db.String(10), nullable=False)
    def __init__(self, login, password):
        self.admin_login = login
        self.admin_password = password


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_name = db.Column(db.String(255), nullable=False)
    post_text = db.Column(db.Text(), nullable=False)
    post_image = db.Column(db.String(255), nullable=False)
    continent = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.Date(), default=datetime.utcnow)
    def __init__(self, name, text, url, continent):
        self.post_name = name
        self.post_text = text
        self.post_image = url
        self.continent = continent

#with app.app_context():
#    db.drop_all()
#    db.create_all()
#    admin= Admin('root', 'root')
#    db.session.add(admin)
#    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/<name>')
def user_index(name):
    return render_template('index.html', user_name=name)

@app.route('/Article')
def Article():
    new_article = Posts.query.all()
    return render_template('article.html', articles = new_article)

@app.route('/Admin', methods = ['GET'])
def Admin_enter():
    return render_template('login_admin.html')

@app.route('/Admin', methods = ['POST'])
def Admin_login():
    login = request.form['login']
    password = request.form['password']
    if Admin.query.filter_by(admin_login=login, admin_password=password).all() != []:
        return render_template('add_article.html')
    else:
        return render_template('login_admin.html')

@app.route('/add_post', methods = ['POST'])
def add_post():
    title = request.form['title']
    text = request.form['text']
    URL = request.form['URL']
    continent = request.form['continent']
    row = Posts(title, text, URL, continent)
    db.session.add(row)
    db.session.commit()
    return render_template('add_article.html')


if __name__ == '__main__':
    app.run()