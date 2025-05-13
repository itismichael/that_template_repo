# Placeholder for your main application logic or FastAPI app

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from pydantic import BaseModel
from your_core_library.data_handler import DataHandler
from your_core_library.data_handler import get_core_greeting

from .config import settings
from .logging_config import init_logging

logger = logging.getLogger(__name__)


# Define Pydantic models here if they are specific to the app
class ExamplePayload(BaseModel):
    data: str


# Lifespan context manager for startup and shutdown events
@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    # Startup logic
    init_logging(settings.LOG_LEVEL)
    logger.info("Application startup sequence started.")
    logger.info(f"Application Name: {settings.APP_NAME}")
    logger.info(f"Application Version: {settings.APP_VERSION}")
    logger.info(f"Log Level: {settings.LOG_LEVEL}")

    # Initialize DataHandler and make it available via app.state
    app_instance.state.data_handler = DataHandler()
    logger.info("DataHandler initialized and attached to app state.")
    logger.info("Application startup sequence complete.")
    yield
    # Shutdown logic (if any)
    logger.info("Application shutdown sequence started.")
    # Clean up resources, e.g., app.state.data_handler.close_connections()
    logger.info("Application shutdown sequence complete.")


# Initialize FastAPI app with lifespan context manager
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A template for Python FastAPI projects with a core library.",
    lifespan=lifespan,  # Use the lifespan manager
)


@app.get("/", tags=["General"])
async def read_root():
    logger.info("Root endpoint was called.")
    return {
        "message": "Hello from FastAPI app! Use /core_greet for core library greeting."
    }


@app.post("/process/", tags=["Processing"], response_model=ExamplePayload)
async def process_data(request: Request, payload: ExamplePayload):
    """
    Processes data using the core library's DataHandler.
    """
    try:
        # Access app.state.data_handler via the request object
        data_handler_from_state = request.app.state.data_handler
        result = data_handler_from_state.process(payload.data)
        return {"data": result}
    except AttributeError:  # Should not happen if lifespan is correct
        logger.error(
            "Critical: data_handler not found on app.state. Check lifespan initialization."
        )
        raise HTTPException(
            status_code=500,
            detail="Internal server error: Core processing component not available.",
        ) from None
    except ValueError as e:
        logger.warning(f"ValueError during data processing: {e}")
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/items/{item_id}", tags=["Items"])
async def read_item(item_id: int):
    logger.info(f"Item endpoint called with item_id: {item_id}")
    # In a real app, you'd fetch item details from a database or other source
    return {
        "item_id": item_id,
        "name": "Sample Item",  # Placeholder name
        "owner": "testuser",  # Placeholder owner
    }


@app.get("/health", tags=["Health"])
async def health_check():
    logger.debug("Health check endpoint was called.")
    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
    }


@app.get("/core_greet")
async def core_greeting_endpoint(name: str = "App User"):
    logger.info(f"Core greeting endpoint called with name: {name}")
    core_msg = get_core_greeting(name)
    logger.debug(f"Core library returned: {core_msg}")
    return {"core_message": core_msg}


# For now, a simple function to demonstrate app layer, independent of core logic for now
def get_app_specific_greeting():
    return "Hello from the App Layer of your_project_name_here!"


if __name__ == "__main__":
    # This is for local execution of this file, not for Uvicorn
    print(get_app_specific_greeting())
    # To run with uvicorn: uvicorn app.main:app --reload
