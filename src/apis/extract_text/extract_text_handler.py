import os
import io
import pytesseract
from PIL import Image
from fastapi import APIRouter, Request, status, UploadFile, HTTPException

from src.schemas.message_schema import MessageResponse


router = APIRouter()


default_mime_types = [
    "image/jpeg",
    "image/png"
]

allowed_mimetypes = os.environ.get('ALLOWED_MIME_TYPES', default_mime_types)


@router.post(
    "/extract-text",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    tags=["OCR"]
)
async def extract_text_handler(request: Request, file: UploadFile):
    """
    Extracts text from an image if the image format is among those accepted.
    """

    logger = request.state.logger

    if file.content_type not in allowed_mimetypes:
        logger.warning('Recived file has a mimetype not allowed')

        raise HTTPException(
            status_code=400,
            detail="Recived file has a mimetype not allowed"
        )

    contents = await file.read()
    image_stream = io.BytesIO(contents)
    image_stream.seek(0)
    image = Image.open(image_stream)

    text_list = pytesseract.image_to_string(image)

    return {"message": text_list}
