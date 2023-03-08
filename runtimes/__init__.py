#!/usr/bin/env python3

import os
from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__)

    @app.get('/')
    def hello_world():
        return {"hello": "world"}

    return app