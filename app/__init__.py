from flask import Flask
from flask_bootstrap import Bootstrap

# Setup App object
app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)

from app import views
