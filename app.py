from datetime import datetime
from flask import Flask, render_template, request, redirect, jsonify, session
from methods import guess_MBTI
from objects import track

import json
import urllib.parse
import requests

app = Flask(__name__)
app.secret_key = 'key'

CLIENT_ID = 'ce45047d36364072a1c99918cc775975'
CLIENT_SECRET = 'e14fb52adc374bbd8677c77b6928b01f'
REDIRECT_URI = 'http://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-read-recently-played'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()
        
        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return redirect('/results')

@app.route('/results')
def get_history():
    if 'access_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh-token')
    
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    response = requests.get(API_BASE_URL + 'me/player/recently-played', headers = headers)

    track_history = json.loads(response.content)
    tracks = []

    for item in track_history["items"]:
        new_track = track(name = item["track"]['name'], id = str(item["track"]['id']), acousticness=0.0,
                          danceability=0.0, energy=0.0, instrumentalness=0.0, liveness=0.0,
                          speechiness=0.0, tempo=0.0, valence=0.0)
        tracks.append(new_track)

    stats = {"acousticness" : 0.0, "danceability" : 0.0, "energy" : 0.0, 
             "instrumentalness" : 0.0, "liveness" : 0.0, "speechiness" : 0.0,
             "tempo" : 0.0, "valence" : 0.0}

    for current_track in tracks:
        fetch = requests.get(API_BASE_URL + 'audio-features/' + current_track.id, headers = headers)
        info = json.loads(fetch.content)

        current_track.acousticness = info['acousticness']
        stats["acousticness"] += current_track.acousticness

        current_track.danceability = info['danceability']
        stats["danceability"] += current_track.danceability
        
        current_track.energy = info['energy']
        stats["energy"] += current_track.energy

        current_track.instrumentalness = info['instrumentalness']
        stats["instrumentalness"] += current_track.instrumentalness

        current_track.liveness = info['liveness']
        stats["liveness"] += current_track.liveness

        current_track.speechiness = info['speechiness']
        stats["speechiness"] += current_track.speechiness

        current_track.tempo = info['tempo']
        stats["tempo"] += current_track.tempo

        current_track.valence = info['valence']
        stats["valence"] += current_track.valence
    
    for feature in stats:
        stats[feature] /= len(tracks)

    mbti = guess_MBTI(stats)
    display = []

    return render_template('results.html', mbti=mbti)

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        print("Refreshing Token...")
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET 
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/results')

if __name__ == "__main__":
    app.run(debug=True)

