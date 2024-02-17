from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/<name>')
def user_index(name):
    return  render_template( 'index.html', user_name=name)

@app.route('/Article1')
def Article():
    return '<h1>Незабаром ви побачите наші статті Stas</h1>'

@app.route('/Admin1')
def Admin():
    return ('<h1>Це адміни<h1><br><p>напишіть наші помилки Stas</p><br> ')
   # return ('<textarea name="text" required rows="15" cols="100" placeholder="Your text"></textarea>')


@app.route('/Login')
def Login():
    return render_template('logo.html')

@app.route('/Add_Article')
def Add_Article():
    return render_template('add_article.html')



if __name__ =="__main__":
    app.run()