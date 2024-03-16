#!/usr/bin/env python3
# 
# -*- coding: utf-8 -*-
__author__ = "Casper Pedersen"
__version__ = "1.0"
__maintainer__ = "Casper Pedersen"
__email__ = ""
__status__ = "Development/Production"


import os
import sys
import datetime

from pythontools.myUtils import eprint

from flask import Flask, request

app = Flask(__name__)
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
@app.route('/')
def hello_world():
    return "<br>Hello World!</b>"

''' ----------------------------------------------- '''
@app.route('/query', methods='GET')
def entities():
    if request.method == 'GET':
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }

@app.route('/song/<int:entity_id>', methods='GET')
def get_song():
    pass

@app.route('/song/<string:artist>', methods='GET')
def get_artist():
    pass

@app.route('/album/<string:album>', method='GET')
def get_album():
    pass


''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''

''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
''' ----------------------------------------------- '''
if __name__== "__main__":
    app.run(debug=True)

''' ----------------------------------------------- '''
