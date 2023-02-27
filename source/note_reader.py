from matplotlib import pyplot
from matplotlib.figure import Figure
import spotipy
import json
import logging
import io


logging.basicConfig(level=logging.INFO)

class Reader():
    def __init__(self, spotify) -> None:
        self.spotify = spotify
        # air g https://open.spotify.com/track/0Kx3zOgcppxtSl1LJNAZml?si=7b53840081e242a3
        self.track = "spotify:track:0Kx3zOgcppxtSl1LJNAZml"

    def get_notes(self):
        audio_info = self.spotify.audio_analysis(self.track)
        song = []
        segments = audio_info["segments"]
        for index in range(len(segments)):
            if segments[index]["confidence"] < 0.7:
                continue
            if segments[index]["duration"] < 0.1:
                continue
            pitches = segments[index]["pitches"]
            timbre = segments[index]["timbre"]
            for note in range(len(pitches)):
                # if pitches[note] < 0.1 or timbre[note] < 0.1:
                #     continue
                song.append((pitches[note], timbre[note]))
        return song

    def print_notes(self, song):
        how_many = 100
        x = [note[0] for note in song]
        y = [note[1] for note in song]
        a = range(1, how_many+1)
        fig = Figure(figsize=(20, 10))
        axis = fig.add_subplot(2,1,1)
        axis.bar(a,y[0:100], edgecolor="black")
        axis = fig.add_subplot(2,1,2)
        axis.bar(a,y[100:200], edgecolor="black")
        return fig
