from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'g12eg12dbdbgyubyd3y'


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


@app.route('/login/<username>/<password>')
def login(username, password):
    session['username'] = username
    session['password'] = password
    return 'yoo'


@app.route('/logout')
def logout():
    # print(session['username'])
    # Deleting key username from the dictionary sessions of the user!!
    woho = session.pop('username', None)
    woho = session.pop('password', None)
    return 'yoo'


if __name__ == '__main__':
    app.run(debug=True)
