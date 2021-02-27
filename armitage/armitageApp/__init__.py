#!/usr/bin/python3

from flask import Flask
from flask_cors import CORS, cross_origin
from .fibonacci.controller.fibonacciController import fibonacci
from .factorial.controller.factorialController import factorial
from .ackermann.controller.ackermannController import ackermann
import flask_monitoringdashboard as dashboard
from .model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func


def create_app(test_config=None):
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__, template_folder='')
    cors = CORS(app)
    dashboard.bind(app)
    app.register_blueprint(fibonacci, url_prefix='/fibonacci')
    app.register_blueprint(factorial, url_prefix='/factorial')
    app.register_blueprint(ackermann, url_prefix='/ackermann')
    engine = create_engine("sqlite:///database.db")
    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.close()

    @app.route('/')
    @cross_origin()
    def index():
        return "Please refer to the endpoint documentation"

    return app
