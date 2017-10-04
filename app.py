# -*- coding: utf-8 -*-

import os
import sys
import json
from bottle import run, route, template, request, static_file, debug

@route('/', method='GET')
@route('/index', method='GET')
@route('/index.htm', method='GET')
@route('/index.html', method='GET')
def index():
  return template(r'base.tpl', titlePage = 'Building a Blockchain')

@route(r'/css/<filename:re:.*\.css>')
def sendCSS(filename):
  return static_file(filename,root='css')
  
@route('/favicon.ico', method='GET')
def get_favicon():
  return static_file('favicon.ico', root='img')
  
@route(r'/img/<filename:re:.*\.(ico|jpg|png|ICO|JPG|PNG)>')
def get_image(filename):
  return static_file(filename, root='img')

@route(r'/fonts/<filename:re:.*\.(eot|svg|ttf|woff|woff2|EOT|SVG|TTF|WOFF|WOFF2)>')
def sendFont(filename):
  return static_file(filename,root='fonts')
  

print('***ПОРТ 8082***')
run(host='localhost', port=8082, debug=True, reloader=True)