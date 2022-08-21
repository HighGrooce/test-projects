from flask import Flask,render_template
import sqlite3
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()


@app.route('/remark')
def remark():
    datalist  = []
    data = pd.read_csv('G:\\work\\testdata\\reviews_midea.csv').reset_index()
    data = np.array(data)
    data = data.tolist()
    for item in data:
        datalist.append(item)
    print(datalist)
    return render_template("remark.html",remarks = datalist)



@app.route('/score')
def score():
    num = []
    temp = pd.read_csv('G:\\work\\testdata\\emotion_one.csv')
    score = temp["amend_weight"].to_list()
    num = [x for x in range(0,2169)]
    return render_template("score.html",score= score,num=num)


@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/tech')
def tech():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
