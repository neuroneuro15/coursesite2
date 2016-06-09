from app import app
import os
from os import path
from glob import glob
from flask import  render_template, url_for, send_from_directory, redirect

slide_dir = path.join(app.static_folder, 'pycourse', 'lessons')
slides = [glob(path.join(slide_dir, dd, '*.slides.html'))[0] for dd in os.listdir(slide_dir)]
slides = sorted(slides)


# Routing
@app.route('/')
def hello_world():
    slide_names = [path.dirname(slide).split('/')[-1].split('_')[1] for slide in slides]
    print(slide_names)
    return render_template('index.html', slides=slide_names)

@app.route('/<int:lecnum>')
def lecture(lecnum):
    return send_from_directory(path.dirname(slides[lecnum-1]),
                               filename=path.basename(slides[lecnum-1]))



@app.route('/format')
def code_format_test():
    return render_template('base.html')
