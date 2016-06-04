from flask import Flask, render_template, url_for, send_from_directory
from flask_bootstrap import Bootstrap
import os
from os import path
from glob import glob


app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)

def count_total_lectures():
    staturl = glob(path.join(app.static_folder, 'lecture*'))
    return len(staturl)


@app.route('/')
def hello_world():
    tot_lectures = count_total_lectures()
    return render_template('index.html', tot_lectures=tot_lectures)

@app.route('/course/<int:lecnum>')
def lecture(lecnum):
    return send_from_directory('static',
                               filename='lecture{}.html'.format(lecnum))