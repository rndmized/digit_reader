var isImageLoaded = false;
// Get a reference to the file select input field
var fileChooser = document.getElementById('fileChooser');

function handleFileSelect(event) {
    // Get the FileList object from the file select event
    var files = event.files;

    // Check if there are files in the FileList
    if (files.length === 0) {
        return;
    }

    // For this example we only want one image. We'll take the first.
    var file = files[0];

    // Check that the file is an image
    if (file.type !== '' && !file.type.match('image.*')) {
        return;
    }

    // The URL API is vendor prefixed in Chrome
    window.URL = window.URL || window.webkitURL;

    // Create a data URL from the image file
    var imageURL = window.URL.createObjectURL(file);

    loadAndDrawImage(imageURL);
}

function loadAndDrawImage(url) {
    // Create an image object. This is not attached to the DOM and is not part of the page.
    var image = new Image();

    // When the image has loaded, draw it to the canvas
    image.onload = function () {
        var canvas = document.getElementById("canvas");
        var context = canvas.getContext("2d");
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.drawImage(image, 0, 0, canvas.width, canvas.height);
        isImageLoaded = true;
    }

    // Now set the source of the image that we want to load
    image.src = url;
}


function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.readAsDataURL(input.files[0]);
    }
}

$("#fileInput").change(function () {
    readURL(this);
    handleFileSelect(this);
    $('.blockquote-footer').text('')
});


$("#submit").click(function (e) {
    e.preventDefault();
    if (isImageLoaded) {
        var canvas = document.getElementById("canvas");
        var image = canvas.toDataURL('image/png');
        $.ajax({
            type: "POST",
            url: "/upload",
            data: image,
            success: function (data) {
                $('.blockquote-footer').text(data.result)
            }
        });
    }
});