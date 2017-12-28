#! /usr/bin/env python
# -*- coding utf-8 -*-

"""
@author:zhangrui
@file:run.py
@time:12/11/17 12:59 PM
"""

import os
from app import create_app
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
manager = Manager(app)
migrate = Migrate(app)

def make_shell_context():
    return dict(app=app)
    manager.add_command("shell",Shell(make_context=make_shell_context))
    manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    