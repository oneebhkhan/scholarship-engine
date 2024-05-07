import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from app.config.config import SOURCE_DB_URI, SOURCE_DB_USER, SOURCE_DB_PASSWORD

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{SOURCE_DB_USER}:{SOURCE_DB_PASSWORD}@{SOURCE_DB_URI}"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

logging.basicConfig()
logger = logging.getLogger("init")
logger.setLevel(logging.DEBUG)

# Placed at bottom to avoid circular dependency
# from .routes import
logger.info("Starting application")