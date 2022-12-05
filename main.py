import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, current_app
from werkzeug.utils import secure_filename
import pandas as pd
import uuid
import json

app = Flask(__name__)

token = os.environ['OAuth']


@app.route("/")
def uploader_file():
  return render_template("index.html")


@app.route("/create")
def createAndSend():
  args = request.args
  playlist_link = args.get("playlist")
  device = args.get("device")
  headers = {"Accept": "application/json", "Authorization": "Bearer " + token}
  res = json.loads(
    requests.get("https://api.spotify.com/v1/playlists/" + playlist_link +
                 "/tracks",
                 headers=headers).text)
  for i in range(0, len(res["items"])):
    imagelist = res["items"][i]["track"]["album"]["images"]

    print(imagelink)
  return "1"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
