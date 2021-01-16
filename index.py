from uploadToGSC import Upload_blob
from speechToText import SpeechToText
from textTone import getResponse
import os
import uuid
import scipy.io.wavfile as wav

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gapi-chrome-extension-bece3debbebd.json"

path = "C:/Workspace/SpeakYourDream/ted.wav"
(source_rate, source_total) = wav.read(path)
totalTime = len(source_total)/float(source_rate)
file_name = str(uuid.uuid1())

Upload_blob(path, file_name)

result = SpeechToText("gs://speakyourdream2086/" + file_name)
noLikes = len(result.split(' like '))-1
totalWords = len(result.split(' '))
print(result)
print("number of likes:", noLikes)
print("words per minute", (totalWords/totalTime) * 60)
print(getResponse(result))
