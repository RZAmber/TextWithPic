#! /usr/bin/env python
# -*- coding：utf-8 -*-

"""
@author:zhangrui
@file:__init__.py.py
@time:12/11/17 12:50 PM
"""

from flask import Blueprint

main = Blueprint('main',__name__)
from . import views


