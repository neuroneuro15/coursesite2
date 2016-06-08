from flask import Flask, render_template, url_for, send_from_directory, redirect
from flask_bootstrap import Bootstrap
import os
from os import path
from glob import glob


# Setup App object
app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)

# Random Functions
def count_total_lectures():
    staturl = glob(path.join(app.static_folder, 'pycourse/lessons/*'))
    print(staturl)
    return len(staturl)


slide_dir = path.join(app.static_folder, 'pycourse', 'lessons')

# Routing
@app.route('/')
def hello_world():
    tot_lectures = count_total_lectures()
    print(tot_lectures)
    return render_template('index.html', tot_lectures=tot_lectures)

@app.route('/<int:lecnum>')
def lecture(lecnum):
    # names = os.listdir(slide_dir)
    names = [glob(path.join(slide_dir, dd, '*.slides.html'))[0] for dd in os.listdir(slide_dir)]
    print(names)
    # return 'success'
    return send_from_directory(path.dirname(names[lecnum-1]),
                               filename=path.basename(names[lecnum-1]))



@app.route('/format')
def code_format_test():
    return render_template('base.html')
