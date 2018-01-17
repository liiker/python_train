# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

def load_data():
    conn = sqlite3.connect('lesson.db')
    coursor = conn.cursor()
    rows = coursor.execute('select * from blog').fetchall()
    return rows

# 装饰器
@app.route('/')
@app.route('/<name>')
def index(name='Eric'):
    posts = load_data()
    print posts
    return render_template('home.html', name=name, posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
