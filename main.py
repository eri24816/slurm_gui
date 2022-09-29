from flask import Flask
from flask_socketio import SocketIO
from flask import request, Flask, Blueprint, flash, g, redirect, render_template,  session, url_for
from src import socketio,create_app
import json

app = create_app()


def run():

    app = create_app()
    socketio.init_app(app)
    app.secret_key = __import__('os').urandom(24)
    socketio.run(app,debug=True,port=int(json.load(open('config.json'))["port"]),ssl_context='adhoc')

if __name__ == '__main__':
    run()
