import pytest


@pytest.mark.parametrize(
    "image_name,mime_type",
    [
        ("image.png", "image/png"),
        ("image.jpg", "image/jpeg"),
        ("image.jpeg", "image/jpeg"),
    ]
)
def test_200_extract_text(test_client, image_name, mime_type):
    """
    Returns a 200 status code and a message when a valid image file
    is uploaded for text extraction.
    """

    image_path = f"tests/unit/src/apis/extract_text/assets/{image_name}"

    with open(image_path, "rb") as image:
        response = test_client.post(
            "/extract-text",
            files={
                "file": (image_name, image, mime_type)
            }
        )

    content = response.json()

    assert response.status_code == 200
    assert isinstance(content, object)
    assert isinstance(content["message"], str)


@pytest.mark.parametrize(
    "image_name,mime_type",
    [
        ("image.bmp", "image/bmp"),
        ("image.pdf", "application/pdf"),
    ]
)
def test_400_extract_text(test_client, image_name, mime_type):
    """
    Returns a 400 status code and an error message when an image file
    with an unsupported mime_type is uploaded.
    """

    image_path = f"tests/unit/src/apis/extract_text/assets/{image_name}"

    with open(image_path, "rb") as image:
        response = test_client.post(
            "/extract-text",
            files={
                "file": (image_name, image, mime_type)
            }
        )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Recived file has a mime type not allowed"
    }
