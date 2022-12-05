import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, current_app
from werkzeug.utils import secure_filename
import pandas as pd
import uuid

app = Flask(__name__)



@app.route("/")
def uploader_file():
  return render_template("index.html")

@app.route("/create")
def createAndSend():
  return 0



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
  