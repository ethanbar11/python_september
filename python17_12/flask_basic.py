from flask import Flask, render_template
import random

app = Flask(__name__)


# @app.route('/')
# def index():
#     import os
#     dir_path = os.getcwd()
#     return render_template('index.html') \
#  \
#  \
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'Hello world!'


@app.route('/bla_bla/<username>')
def bla(username):
    print('This is the user name : {}'.format(username))
    return 'Hello to you Mr. {}'.format(username)


def print_woho():
    print('woho')


@app.route('/')
def get_num():
    num = random.randint(1, 10)
    print('The number for the client is : {}'.format(num))
    return 'Your number is : {} '.format(str(num))
    # print_woho()
    # return 'woho'
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
