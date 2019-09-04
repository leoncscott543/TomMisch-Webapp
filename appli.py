# this is the main executable file 
# I built a route that sends song data 
# (fetched from genius) to the page.html templates file
# to use the data dynamically on the page

from flask import Flask, render_template
import os
import requests
import json
import random

# app execution name is appli
appli = Flask(__name__)

# defining authorization header in myheader :)
myheader = {"Authorization": "Bearer eTnvJMtGEvFKJVrj72lNjVZzXgtyE1xD6Q-Unv2A0Amjhgfx-DEo-1oEUnipH87b"}

# multiple songs to randomly generate
song_id = [3300945, 2275793, 730]

# retreiving song api from genius and converting to json
song = requests.get('https://api.genius.com/songs/' + str(random.choice(song_id)) + '?text_format=plain', headers=myheader)
song_json = song.json()

# just print(song_string) to inspect json data tree
song_string = json.dumps(song_json, indent=2) 

# main route, returns .json api data to page.html 
# uses render_template to access page.html
@appli.route("/")
def songdata():
    return render_template('page.html', 
    song_art= song_json['response']['song']['song_art_image_url'],
    song_fulltitle = song_json['response']['song']['full_title']
)

appli.run(host=os.getenv('IP', '0.0.0.0'), 
          port=int(os.getenv('PORT', 8080)),
          debug=True)