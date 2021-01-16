# Imports the Google Cloud client library
from google.cloud import speech

def SpeechToText(url):
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    gcs_uri = url

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        audio_channel_count=2
    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)
    string = ""

    for result in response.results:
        line = result.alternatives[0].transcript
        if(line[0] == " "):
            line = line[1:]
        string += line.capitalize() + ". "
    return string