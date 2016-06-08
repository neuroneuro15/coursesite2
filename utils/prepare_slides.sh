#!/bin/sh

# Converts all ipynb files to slides.html for rendering on a web page
LESSONDIR='../app/static/pycourse/lessons'
for dir in $LESSONDIR/*; do
    echo Converting $dir "..."
    cd $dir
    jupyter nbconvert --to slides --reveal-prefix "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.1.0" *.ipynb
    cd -
done