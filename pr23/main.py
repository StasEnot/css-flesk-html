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

class Role(db.Model):
      __table=name__ = 'roles'
      id = db.Column(db.Integer,primary__kry=True)
      name = db.Column(db.String(64), unique=True)
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