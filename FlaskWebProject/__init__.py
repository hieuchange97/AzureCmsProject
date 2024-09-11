"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# TODO: Add any logging levels and handlers with app.logger
# Create a stream handler
streamHandler = logging.StreamHandler()

# Set the logging level for the stream handler to match the application's logging level
streamHandler.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the stream handler
streamHandler.setFormatter(formatter)

# Add the file handler to the logger
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
