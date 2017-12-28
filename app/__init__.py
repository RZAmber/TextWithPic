#! /usr/bin/env python
# -*-coding utf-8 -*-

"""
@author:zhangrui
@file:__init__.py.py
@time:12/11/17 12:45 PM
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER']='uploads/'
    app.config['ALLOWED_EXTENSIONS'] = set(['txt','pdf','png','jpg','jpeg','gif'])
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app.run(host='0.0.0.0',port=8000)