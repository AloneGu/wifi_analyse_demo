# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from distribution_check import get_wifi_data
@app.route('/')
@app.route('/index')
def index():
    names,values = get_wifi_data()
    return render_template("index.html",
        title = 'Home',
        wifi_names = names,
        wifi_values = values)