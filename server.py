from speechModule.textToSpeech import convertTextToSpeech
from flask import Flask, render_template, request, url_for

app = Flask("textToSpeech")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate_audio():
    audio_path = None

    if request.method == 'POST':
        # Access paragraph input from the form
        paragraph = request.form['paragraph']

        convertTextToSpeech(paragraph)

        # Set the audio path
        audio_path = url_for('static', filename="audio/output.mp3")

    # Render the HTML template with the audio element
    return render_template('index.html', audio_path=audio_path)

if __name__ == '__main__':
    app.run(debug=True,port = 5000)
