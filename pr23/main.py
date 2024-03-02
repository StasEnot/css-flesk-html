import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Administarator_data(db.Model):
      __tablename__ = 'administarator_data'
      id = db.Column(db.SmallInteger(),primary_key=True)
      login = db.Column(db.String(64), unique=True, nullable=False)
      pasasword = db.Column(db.SmallInteger(), nullable=False)


class article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    text = db.Column(db.Text(900), unique=True)
    images = db.Column(db.Text(128), unique=True, nullable=False)
    Continent = db.Column(db.String(12))
    data = db.Column(db.Date(), unique=True, nullable=False)




@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/<name>')
def user_index(name):
    return render_template( 'index.html', user_name=name)

@app.route('/Article1')
def Article():
    new_artilce = ['How to avoid expensive travel mistakes',
                   'Top 5 places to experience supernatural forces',
                   'Three wonderfully bizarre Mexican festivals',
                   'The 20 greenest destinations on Earth',
                   'How to survive on a desert island']
    return render_template('article.html', articles=new_artilce)

@app.route('/Admin1')
def Admin():
    return render_template('login_admin.html')


@app.route('/Login')
def Login():
    return render_template('login.html')

@app.route('/Add_Article')
def Add_Article():
    return render_template('add_article.html')

if __name__ =="__main__":
    app.run()