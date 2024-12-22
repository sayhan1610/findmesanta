from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def static_files(filename):
    folder_path = os.path.join(app.root_path, '.')
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(debug=True)
