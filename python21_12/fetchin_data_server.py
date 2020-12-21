from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/home.html',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        print(name, email)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
