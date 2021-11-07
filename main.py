import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from settings import get_settings


settings = get_settings()

app = FastAPI()


@app.get('/')
async def root():
    """Say hello."""
    return HTMLResponse('<h1>Hello FastAPI</h1>')


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.host,
        port=settings.port,
        reload=True,
        reload_includes=['*.py', '*.html', '*.css'],
    )
