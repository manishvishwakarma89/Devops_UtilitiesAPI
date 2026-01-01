from app.api import app
import uvicorn

if __name__ == "__main__":
    # ASGI Web Server
    uvicorn.run(
        "app.api:app",
        host="1270.0",
        port=8000,
        reload=True
    )