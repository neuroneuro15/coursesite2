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

    # return render_template('Python Course Lecture 2.slides.html')
    # return app.send_static_file('lecture1s.html')
    # return render_template('lecture1.html')

    #   jupyter nbconvert --to slides Note: when converting to slides in nbconvert, remember to add
    # --reveal-prefix "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.1.0"

    # slides = glob(path.join(slide_dir, '*.slides.html'))
    # slides = [path.basename(name) for name in sorted(slides)]
    # print(slides)
    # print(slides[lecnum - 1])
    new_path = path.join(slide_dir, 'Errors/')
    print(new_path)
    return send_from_directory(new_path, filename='lecture7a.slides.html')



@app.route('/format')
def code_format_test():
    return render_template('pretty.html')
