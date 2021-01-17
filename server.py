from flask import Flask, render_template, send_file, redirect, request
import wave

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/stats')
def stats():
   return render_template('stats.html')

@app.route('/save', methods=['POST'])
def save():
    f = request.files['audio_data']

    with open("audio.wav", 'wb') as audio:
        f.save(audio)
    return "success"
if __name__ == '__main__':
    app.run(debug=True)

