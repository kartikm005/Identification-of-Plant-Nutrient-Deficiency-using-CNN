import gtts
from playsound import playsound


tts1 = gtts.gTTS("Detected As Cover Image",lang='en',tld='co.in')
tts1.save("cover.mp3")
playsound("cover.mp3")

tts1 = gtts.gTTS("Detected As Stego Image",lang='en',tld='co.in')
tts1.save("stego.mp3")
playsound("stego.mp3")

