from flask import Flask, flash, redirect, render_template, \
     request, url_for, redirect
import os
from werkzeug.utils import secure_filename

PATH_DEFAULT = 'C:/Users/OS/Desktop/Data/0.Work/nickgame/nick_game/30.App/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/nicks/'

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def upload_file(image, path, file_old=None):
    file_name = UPLOAD_FOLDER + image.filename[0:len(image.filename)]
    filename = image.filename[2:len(image.filename)]
    filename = '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    if file_old:
        os.remove(os.path.join(PATH_DEFAULT, file_old))
    if image and filename:
        filename = secure_filename(image.filename)
        image.save(os.path.join(path, filename))
    return file_name
