#!/usr/bin/env python3

from flask import Flask
# name is the name of the current module
app = Flask(__name__)


@app.route('/') #this app.route decorator tells Flask to show the returned data from index to the web broswser.
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<string:username>') #we add string: to amke sure the username is a valid string, can also use int, float, or path
def user(username):
    return f'<h1>Profile for {username}</h1>'


#add this line so we can run script with 'python app.py'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
