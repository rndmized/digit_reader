# Source: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
# Adapted from / References:
# https://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white

import os
import numpy as np
import PIL.Image as pil
import PIL.ImageOps as pilOps
from flask import Flask, request, redirect, url_for, render_template, flash, json, jsonify
from model import model
import re
import base64
import tensorflow as tf

app = Flask(__name__)

x = tf.placeholder("float", [None, 784])
sess = tf.Session()

with tf.variable_scope("deep-learning"):
    keep_prob = tf.placeholder("float")
    y2, variables = model.mmodel(x, keep_prob)
save = tf.train.Saver(variables)
save.restore(sess, "model/deep-learning.ckpt")

def testModel(image):
    return sess.run(y2, feed_dict={x: image, keep_prob: 1.0}).flatten().tolist()

# Parse Image - Handed out by a classmate
def parseImage(imgData):
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('static/images/TestImage.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

@app.route('/', methods=['GET', 'POST'])
def root():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # Read Image from request
    # Parse the image into the folder before read
    parseImage(request.get_data())
    # Format image properly
    # Open Image
    image = pil.open('static/images/TestImage.png')
    # Resize Image
    image = image.resize([28,28],resample=pil.LANCZOS)
    # Convert to Grayscale
    image_gray = image.convert(mode='L')
    # Invert Colors
    image_gray = pilOps.invert(image_gray)
    # Clean thresholds
    bw = image_gray.point(lambda x: 0 if x<128 else 255, '1')
    # Display Image for testing purposes
    bw.show()
    # Run model
    test_image = ((255 - np.array(bw, dtype=np.uint8)) / 255.0).reshape(1, 784)
    result = testModel(test_image)
    # Return result
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
    