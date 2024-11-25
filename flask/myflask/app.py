from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is about page.'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def num():
    username = request.form['username']
    return f'hello, {username}!'


if __name__ == '__main__':
    app.run(debug=True)