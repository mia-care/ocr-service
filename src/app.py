import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from src.middlewares.logger_middleware import LoggerMiddleware

from src.apis.core.liveness import liveness_handler
from src.apis.core.readiness import readiness_handler
from src.apis.core.checkup import checkup_handler
from src.apis.extract_text import extract_text_handler


load_dotenv('default.env')

app = FastAPI(
    openapi_url="/documentation/json",
    docs_url=None,
    redoc_url=None
)

# The Swagger Aggregator is compatible with 3.0.X OpenAPI schemas versions
app.openapi_version="3.0.2"

# Middlewares
app.add_middleware(LoggerMiddleware)

# Core
app.include_router(liveness_handler.router)
app.include_router(readiness_handler.router)
app.include_router(checkup_handler.router)

# OCR
app.include_router(extract_text_handler.router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=int(os.environ.get('HTTP_PORT', 3000)),
        log_config=None
    )
