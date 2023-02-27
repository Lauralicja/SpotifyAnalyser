from flask import Flask, Response
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from note_reader import Reader
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

app = Flask(__name__)
app.env = "development"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
rondo_alla_turca = "spotify:track:1iR34ZbPs3eFniMpnrHI6s"

reader = Reader(spotify)

@app.route("/")
async def home():
    return {"text":"Welcome to spotify analyse note something something!"}


@app.route("/analysis", methods=["GET"])
async def analysis():
    return spotify.audio_analysis(rondo_alla_turca)

@app.route("/notes.png", methods=["GET"])
async def notes():
    song = reader.get_notes()
    fig = reader.print_notes(song)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
        
@app.route("/track", methods=["GET"])
async def track():
    return spotify.track(rondo_alla_turca)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

