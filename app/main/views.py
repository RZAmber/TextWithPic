#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:zhangrui
@file:views.py
@time:12/11/17 8:45 AM
"""
from flask import Flask, request,render_template,redirect,url_for,jsonify

from . import main
from TextPic import TextPic
import sys
sys.path.append('D:\\pycharm\\TextWithPic\\app')



@main.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['textarea']
        if sentence != " ":
            data = TextPic().run(sentence)
            return render_template('base.html',data = data, sentence = sentence)
            # return redirect(url_for('main.index',json_str = json_str))
    return render_template('base.html')



