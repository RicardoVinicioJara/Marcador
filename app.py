from flask import Flask, render_template, request, redirect, url_for, flash
import json


app = Flask(__name__)

app.secret_key = "mysecretkey"



@app.route("/")
def index():
    return render_template("login.html")


@app.route("/celular")
def celular():
    return render_template("celular.html")


@app.route("/pantalla")
def pantalla():
    return render_template("pantalla.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.100.10', port=5001)