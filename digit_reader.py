# Source: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
# Adapted from / References:
# https://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white

import numpy as np
import PIL.Image as pil
from flask import Flask, request, redirect, url_for, render_template, json, jsonify
from model import model
import re
import base64
import tensorflow as tf

app = Flask(__name__)

# Create tensorflow placeholders and load stored values from trained session
x = tf.placeholder("float", [None, 784])
sess = tf.Session()

with tf.variable_scope("deep-learning"):
    keep_prob = tf.placeholder("float")
    y, variables = model.mmodel(x, keep_prob)
save = tf.train.Saver(variables)
save.restore(sess, "model/deep-learning.ckpt")

# Funtion to predict the number based on an image array
def predict(image):
    prediction = tf.argmax(y, 1)
    return prediction.eval(feed_dict={x: image, keep_prob: 1.0}, session=sess)

# Parse Image - Handed out by a classmate
def parseImage(imgData):
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('static/images/TestImage.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

# Returns image array with the "proper" 
# format to be read by the prediction function.
def setupImage(image):
    # Resize Image and convert it to grayscale
    image = image.resize([28,28],resample=pil.LANCZOS).convert(mode='L')
    image_array = np.ndarray.flatten(np.array(image)).reshape(1, 784)
    # Detect whether is black & white or viceversa
    color = 0
    # Take coloer from first and last row of pixels and add them all together
    for pix in range(0,28):
        color += image_array[0][pix]
        color += image_array[0][-pix]

    # Since there is going to be noise in the white background pictures
    # Average the background being at least 2/3 white-ish
    # Remove "noise" from image setting values to be either white or black
    # depending on the color of the background
    if (color/2) < ((255*42)/2):
        # print('Black Background')
        for pix in range(0,784):
            if image_array[0][pix] < 150:
                image_array[0][pix] = 0
            else:
                image_array[0][pix] = 255
    else:
        # print('White Background')
        for pix in range(0,784):
            if image_array[0][pix] > 150:
                image_array[0][pix] = 0
            else:
                image_array[0][pix] = 255

    return image_array
    
# Return main page
@app.route('/', methods=['GET', 'POST'])
def root():
    return app.send_static_file('index.html')

# Take image from request and return prediction for that image
@app.route('/upload', methods=['POST'])
def upload_file():
    # Read Image from request
    # Parse the image into the folder before read
    parseImage(request.get_data())
    # Format image properly
    # Open Image
    image = pil.open('static/images/TestImage.png')
    result = predict(setupImage(image))
    return jsonify(result = str(result[0]))


if __name__ == '__main__':
    app.run(debug=True)
    