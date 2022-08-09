import flask
from flask import request, Response,Flask, Blueprint, flash, g, redirect, render_template,  session, url_for
import requests
from flask_socketio import SocketIO

from slurm_gui.main import app, socketio

@app.route('/proxy/<path:url>', methods=["GET", "POST"])
def _proxy(url):
    resp = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


