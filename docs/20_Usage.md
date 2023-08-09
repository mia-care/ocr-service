# OCR Usage

This microservice expose only one endpoint. Below there is a description of how it works.

## POST /extract-text

To extract text from an image, make a POST request to the `/extract-text` endpoint with the image file attached. The microservice will return a JSON object containing the extracted text.

**Request**

To try the following request, go to `/assets/images` folder and run the following curl in your terminal

      curl -X 'POST' \
        'http://0.0.0.0:3000/extract-text' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@ocr-hello-world-sample.png;type=image/png'

**Response**

The microservice will respond with the extracted text.

      { "message": "Hello world\n\f" }
