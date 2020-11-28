from flask import Flask
from projectApp.views import app
from projectApp import models

models.db.init_app(app)