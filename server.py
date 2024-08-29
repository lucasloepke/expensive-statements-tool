import os
from flask import Flask, request, render_template
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

port = int(os.environ.get('PORT', 3000))

@app.route('/')
def index(name='User'):
    return render_template('index.html', person=name, updone=False)

@app.route('/download', methods=['POST'])
def postup(updone=True):
    if 'file1' not in request.files or 'file2' not in request.files:
        return 'No file found', 400
    file1 = request.files['file1']
    file2 = request.files['file2']
    # rename filenames
    if file1.filename == '' or file2.filename == '':
        return 'No file selected', 400
    
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
    file1.save(file1_path)
    file2.save(file2_path)

    # esmain()

    return render_template('download.html', updone=True, f1=file1_path, f2=file2_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
