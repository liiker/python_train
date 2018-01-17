# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)

# 装饰器
@app.route('/')
@app.route('/<name>')
def index(name='Eric'):
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
