from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/Article1')
def Article():
    return '<h1>Незабаром ви побачите наші статті Stas</h1>'

@app.route('/Admin1')
def Admin():
    return '<h1>Це адміни<h1><br><p>напишіть наші помилкиStas</p><br> '

if __name__ =="__main__":
    app.run()