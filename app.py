import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
 naslovSpiska="Restorani"
 #spisakRestorana = ["Gros", "ABC", "Bavka", "Princ"]
 con = sqlite3.connect('dostavahrane.db')

 cur = con.cursor()
 cur.execute("SELECT id,naziv FROM restoran LIMIT 10")

 restoran = cur.fetchall()
 return render_template("index.html",
               naslov = naslovSpiska,
               spisak = restoran)
@app.route("/restoran/<id_rest>")
def restoran(id_rest):
 naslovSpiska="Restoran"
 con = sqlite3.connect('dostavahrane.db')

 cur = con.cursor()
 query = f"select naziv from meni where id_restorana=={id_rest}"
 cur.execute(query)
 jela = cur.fetchall()
 return render_template("restoran.html",
               naslov = naslovSpiska,
               spisak = jela)

@app.route("/primer-string")
def string():
  return "ovo be mno dugacak testk"

@app.route("/primer-broj")
def broj():
  return 265

@app.route("/primer-niz")
def niz():
  nekiNiz = [1,2,3,4,5]
  return nekiNiz

@app.route("/primer-json")
def primerJson():
  data = {
    "message": "This is a JSON response",
    "status": "success"
  }
  return (data)

@app.route ("/primer-html")
def primerHTML():
  data = """<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,
initial-scale=1.0">
   <meta http-equiv= "X-UA-Compatible" content="ie=edge">
   <title>Document</title>
   <link rel="stylesheet" href="static/style.css">
</head>
<body>
   <h1>Zdravo brt</h1>
</body>
</html>"""
  return data
  if __name__ == '__main__':
    app.rn()
