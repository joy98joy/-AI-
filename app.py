from flask import Flask, render_template

import math

app = Flask(__name__)



@app.route('/')

def hello_world():

    return "Hello, DevOps!"

@app.route('/menu')

def menu():

# 'templates' 폴더 안에 'menu.html' 파일이 있다고 가정

    return render_template('menu.html')




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080)