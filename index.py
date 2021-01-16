from uploadToGSC import Upload_blob
from speechToText import SpeechToText
from textTone import getResponse
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gapi-chrome-extension-bece3debbebd.json"

path = "C:/Workspace/SpeakYourDream/ted.wav"
fullpath_name = path.split(".")[0].split("/")
file_name = fullpath_name[len(fullpath_name)-1]

Upload_blob(path, file_name)

result = SpeechToText("gs://speakyourdream2086/" + file_name)
print(getResponse(result))