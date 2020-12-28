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
        address = request.form['address']
        amount = request.form['amount']
        topping = request.form['topping']
        print('name : {} address :{} amount : {} topping : {}'.format(name,address,amount,topping))
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
