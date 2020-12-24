from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello!'


@app.route('/validate_snake', methods=['POST', 'GET'])
def validate_snake():
    d = request.get_json()
    if 'snake' in d:
        return 'Thank you!'
    return 'sssssssssssssssssss'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home.html', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        print('Your name is {} and your email is : {}'.format(name, email))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
