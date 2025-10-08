import os
from flask import Flask, request, render_template, redirect, url_for, flash
import time
from werkzeug.utils import secure_filename
from beat_analyzer import get_bpm

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'flac', 'm4a'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'supersecretkey' # Needed for flashing messages

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            bpm = get_bpm(file_path)
            
            # A small delay to ensure the loading spinner is visible on fast machines
            time.sleep(1)

            if bpm:
                result = render_template('index.html', bpm=bpm, filename=filename)
            else:
                flash(f'Could not analyze BPM for {filename}.')
                result = redirect(request.url)
            
            # Clean up the uploaded file in a try-finally block
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error removing file {file_path}: {e}")

            return result
    return render_template('index.html', bpm=None)

if __name__ == '__main__':
    # Use host='0.0.0.0' to make it accessible on your local network
    app.run(debug=True, host='0.0.0.0')