from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('base.html')
