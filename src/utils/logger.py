import os
import sys
import logging
from dotenv import load_dotenv


load_dotenv('default.env')

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.propagate = False

multipart_logger = logging.getLogger('multipart')
multipart_logger.propagate = False

PIL_logger = logging.getLogger('PIL')
PIL_logger.propagate = False

logging.basicConfig(
    stream=sys.stdout,
    level=os.environ.get('LOG_LEVEL', logging.DEBUG),
)

logger = logging.getLogger('mialogger')
