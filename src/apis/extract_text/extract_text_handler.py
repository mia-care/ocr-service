import io
import pytesseract
from PIL import Image
from fastapi import APIRouter, status, UploadFile, HTTPException

from src.apis.schemas.message_schema import MessageResponse


router = APIRouter()


allowed_mimetypes = {
    "image/jpeg",
    "image/png"
}


@router.post(
    "/extract-text",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    tags=["OCR"]
)
async def extract_text_handler(file: UploadFile):
    """
    TODO
    """

    if file.content_type not in allowed_mimetypes:
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
