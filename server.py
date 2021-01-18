from flask import Flask, render_template, send_file, redirect, request, url_for
import wave
import uuid
import os
from feedback import predictText
from basicStats import getWPM, getRepitition
from readability import flesch
from emotions import detectEmotion
from silence import getPauses
from pronounciation import recognize_from_file
from finalScore import getFinalScore
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stats/<id>')
def stats(id):
    #either create new file to store stats or use existing
    results ={}
    text = open(id+'/transcript.txt', 'r').read()
    audio_path = id+"/audio.wav"
    results['category'] = predictText(text)
    print(results["category"])
    results['readability']=int(flesch(text))
    results['wpm'] = int(getWPM(text,audio_path))
    results['repetition'] = getRepitition(text)
    results['pauses']=int(getPauses(id))
    results['emotion'] = detectEmotion(id)
    #longer emotion bar for more dtected emotions
    results['pronounciation']=int(recognize_from_file(text,audio_path))
    results['fillers']=int(open(id+'/filler.txt', 'r').read())
    print(results)
    results['score']=int(getFinalScore(results['emotion'],results['pronounciation']/100,results['category'],results['pauses'],results['fillers'],results['wpm'],results['readability']/100)*100)
    results['transcript']=text
    print(results)
    return render_template('stats.html',results=results)

@app.route('/save', methods=['POST'])
def save():
    f = request.files['audio_data']
    transcript=request.form['transcript']
    folder = str(uuid.uuid4())
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(folder+"/audio.wav", 'wb') as audio:
        f.save(audio)
    f = open(folder+"/transcript.txt", "a")
    f.write(transcript)
    f.close()
    f = open(folder+"/filler.txt", "a")
    f.write(request.form["filler"])
    f.close()

    return folder
if __name__ == '__main__':
    app.run(debug=True)

