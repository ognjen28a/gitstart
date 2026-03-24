import os
import sqlite3
from flask import Flask, request, jsonify, json
from flask-cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
  return "Zdravo"


if __name__ == '__main__':
  app.run()
