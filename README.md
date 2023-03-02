## Some spotify project for analysis

Im trying to read notes from song using `spotipy` and make them into actual music sheets.
using Air on G by Bach and Spring by Vivaldi.

For now it looks like this, very unsure on how this library interprets pitch/timbre. will see :shrug:

![graph](air.png)


### More about analysis can be found in notebook! ~ :sparkle: Work in progress :sparkle: ~

Why Spring and Air on G?

I used to play violin, so I know a little bit of music theory. Those two are perfect examples of simple classics. They don't compose of too complex techniques, mostly they are played on onne string at a time, which would make it easier for `spotipy.audio_analyse()` to work properly.

Additionally, both of those songs are played on contary strings, making the separation between lower and higher notes easy.

What's more it's the fact that both of them are being played exactly in scale, according to the key; without any romanticism - a very classic approach.