# Source: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

import os
import numpy as np
from PIL import Image
from flask import Flask, request, redirect, url_for, render_template, flash, json, jsonify
from model import model
import re
import base64
from scipy.misc import imread, imresize
import tensorflow as tf


UPLOAD_FOLDER = '/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Parse Image   
def parseImage(imgData):
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('static/images/ImageResult.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

@app.route('/', methods=['GET', 'POST'])
def root():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # Parse the image into the folder before read
    parseImage(request.get_data())


if __name__ == '__main__':
    app.run(debug=True)
    