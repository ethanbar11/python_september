from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
#     import os
#     dir_path = os.getcwd()
#     return render_template('index.html') \
#  \
#  \
@app.route('/hello')
def hello():
    return 'Hello world!'


@app.route('/bla_bla/<username>')
def bla(username):
    print('This is the user name : {}'.format(username))
    return 'Hello to you Mr. {}'.format(username)


if __name__ == '__main__':
    app.run(debug=True)
