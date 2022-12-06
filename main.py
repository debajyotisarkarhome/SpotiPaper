import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, current_app
from werkzeug.utils import secure_filename
import pandas as pd
import uuid
import json
from PIL import Image, ImageEnhance

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
  res = requests.get("https://api.spotify.com/v1/playlists/" + playlist_link +
                     "/tracks",
                     headers=headers)
  print(res.status_code)
  if (res.status_code == 200):
    resinjson = json.loads(res.text)
    imagelist = []
    for i in range(0, len(resinjson["items"])):
      imagelist.append(resinjson["items"][i]["track"]["album"]["images"][0]["url"])
    numofimages = len(imagelist)
    singleres = int(((1080*1920)/15)**0.5)
    #return(imagelist)
    if(device=="mobile"): 
      collage = Image.new("RGBA", (1080,1920))
    else:
      collage = Image.new("RGBA", (1920,1080))
    
    for i in range(0,numofimages):
      singlephoto = Image.open(requests.get(imagelist[i], stream=True).raw).convert("RGBA")
      singlephoto = singlephoto.resize((singleres,singleres))  
      collage.paste(singlephoto,(i*singleres,0))
    collage.show()
    return("1")
  else:
    return("Error Meow")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
