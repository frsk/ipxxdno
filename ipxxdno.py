#!/usr/bin/python3

from flask import make_response, Flask, url_for, request
from time import time

app = Flask(__name__)

def _get_data(request):
  _result = {}
  if 'X-Real-Ip' in request.headers:
    _result['ip'] = request.headers['X-Real-Ip']
  else:
    _result['ip'] = 'N/A'
  if 'User-Agent' in request.headers.keys():
    _result['user-agent'] = request.headers['User-Agent']
  else:
    _result['user-agent'] = 'Unknown User-Agent'
  _result['timestamp'] = ts = int(time())
  return _result

@app.route("/health")
def health():
    return "OK"

@app.route("/")
def index():
    response = make_response("{ip}\n{user-agent}\n{timestamp}\n".format(**_get_data(request)))
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route("/json")
def json():
    response = make_response(_get_data(request))
    response.headers['Content-Type'] = 'application/json'
    return response
    #return(_get_data(request), header{"Content-Type", "application/json"})

@app.route("/dump")
def dump():
    response = make_response(str(request.headers))
    response.headers['Content-Type'] = 'text/plain'
    return response
