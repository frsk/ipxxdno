#!/usr/bin/python3

from flask import make_response, Flask, url_for, request
from time import time

from os import environ

import ipaddress

app = Flask(__name__)

def _get_data(request):
  _result = {}
  if environ['IP_HEADER'] != "False":
    if environ['IP_HEADER'] in request.headers:
        _result['ip'] = request.headers[environ['IP_HEADER']]
  else:
    remote_addr = ipaddress.IPv6Address(request.remote_addr)
    if remote_addr.ipv4_mapped:
      _result['ip'] = remote_addr.ipv4_mapped.compressed
    else:
      _result['ip'] = remote_addr.compressed

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
    if 'Accept' in request.headers.keys():
        if request.headers['Accept'] == 'application/json':
            return json()
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
