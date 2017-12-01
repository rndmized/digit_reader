# Digit Reader
***

Project for Emerging Technologies Module (4th Year, Bsc (Hons) in Software Development). More details about its requirements [here](https://emerging-technologies.github.io/problems/project.html).

## Overview
***

This is a simple web application built in flask that allows a user to upload an image of single digit and get the recognised number in return. It uses the model for deep learning presented on the tensorflow [tutorial](https://www.tensorflow.org/get_started/mnist/pros) that has an expected accuracy of 99.2%. However, even though that is true for images belonging to the MNIST test set (or even the training set) the images uploaded by the user might not have enough quality or might be not centered reducing the accuracy of the model. Some sample images are provided for testing in the Image Samples folder.

![Example GIF](https://github.com/rndmized/digit_reader/blob/master/Assets/Example.gif)

## Requirements
***

This project uses the following technologies in order to work:

* Python
    * Flask
    * Tensorflow
    * Pillow 
    * Numpy
* Javascript
    * JQuery
* HTML5
* Bootstrap 4.0

In order to install python modules you can run the folowing code in the console:

```
$: pip install -r requirements.txt
```

## Running the code

Once the repository has been cloned you can run the server by navigating on the command line to the root directory of the repo and typing:

```
$: python digit_reader.py
```
That will start the server on [localhost:5000](http://localhost:5000/)

## Architecture
***

### Back-end
<p align="center">
<img src="https://www.oakcity.io/wp-content/uploads/2017/04/flask-logo-overview-oak-city-labs-mobile-app-development-company-raleigh-durham.png" width="350"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/TensorFlowLogo.png" width="250">
</p>

The server (backend) uses flask to create a minimal API with two routes: 
* root: returns the html page to be rendered.
* "/upload": Requires POST method. Provided the image sent is the correct type (that should be handled by the javascrip in the front-end) it formats the image to aproximate it to the MNIST format and then uses the model to output back to the front-end the value that represents such image.
### Front-end

<p align="center">
<img src="https://bilalamjad.net/wp-content/uploads/2015/07/bs.png" width="225"><img src="https://cms-assets.tutsplus.com/uploads/users/71/courses/916/preview_image/jquery-3.png" width="260">
</p>

The front-end is an HTML page where the user can upload an image (PNG) and send it to the server in order to get back the digit the image represents. In order to get maximum accuracy the digit in the image must be clear, centered, and avoid as much as possible noise in the image.

## Built with
***
* [Pingendo](https://pingendo.com/)
* [Visual Studio Code](https://code.visualstudio.com/)

## Authors
***

* **Albert Rando** - *Design and Development* - [rndmized](https://github.com/rndmized)


## License
***

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/rndmized/digit_reader/blob/master/LICENSE) file for details)