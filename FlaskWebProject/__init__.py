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
# Remove all existing handlers associated with the logger
app.logger.handlers.clear()

# Set the logging level for the logger itself to INFO
app.logger.setLevel(logging.INFO)

# Create a StreamHandler to output to sys.stderr
streamHandler = logging.StreamHandler()

# Set the logging level for the stream handler to match the application's logging level
streamHandler.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the stream handler
streamHandler.setFormatter(formatter)

# Add the stream handler to the logger
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
