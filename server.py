from flask import Flask, render_template, send_file, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/stats')
def stats():
   return render_template('stats.html')

@app.route('/ezzat')
def ezzat():
    return render_template('ezzat.html')

if __name__ == '__main__':
    app.run(debug=True)
