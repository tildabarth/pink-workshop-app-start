import os
import typing as t
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings


# Load environment variables
load_dotenv()


class Settings(BaseSettings):
    host: str = os.getenv('HOST', '0.0.0.0')
    port: int = os.getenv('PORT', 8000)
    datetime_format: str = os.getenv('DATETIME_FORMAT', '%Y-%m-%dT%H:%M:%SZ')
    static_dir: str = os.getenv('STATIC_DIR', 'app/static')
    templates_dir: str = os.getenv('TEMPLATES_DIR', 'app/templates')
    api_base_url: str = os.getenv('API_BASE_URL', '')
    attributions: t.Tuple[str, ...] = (
        'Icons made by <a href="https://www.flaticon.com/authors/good-ware"' \
        'title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com"' \
        'title="Flaticon">www.flaticon.com</a>',
        'Icons made by <a href="https://www.flaticon.com/authors/iconixar"' \
        'title="iconixar">iconixar</a> from <a href="https://www.flaticon.com"' \
        'title="Flaticon">www.flaticon.com</a>',
        'Icons made by <a href="https://www.freepik.com" title="Freepik">' \
        'Freepik</a> from <a href="https://www.flaticon.com" title="Flaticon"'
        '>www.flaticon.com</a>',
        'Icons made by <a href="" title="Nhor Phai">Nhor Phai</a> from <a href=' \
        '"https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>',
        'Photo by <a href="https://unsplash.com/@fitmasu?utm_source=unsplash&utm_' \
            'medium=referral&utm_content=creditCopyText">Fitsum Admasu</a> on <a href="' \
            'https://unsplash.com/images/things/health?utm_source=unsplash&utm_medium=' \
            'referral&utm_content=creditCopyText">Unsplash</a>',
        'Photo by <a href="https://unsplash.com/@hannaeberh?utm_source=unsplash&utm_medium=' \
            'referral&utm_content=creditCopyText">Hanna Eberhard</a> on <a href="https://unsplash' \
            '.com/images/things/health?utm_source=unsplash&utm_medium=referral&utm_content=creditCopy' \
            'Text">Unsplash</a>',
        'Photo by <a href="https://unsplash.com/@esdesignisms?utm_source=unsplash&utm_medium=' \
            'referral&utm_content=creditCopyText">Emma Simpson</a> on <a href="https://unsplash.' \
            'com/s/photos/running-runner-morning?utm_source=unsplash&utm_medium=referral&utm_content' \
            '=creditCopyText">Unsplash</a>',
    )


@lru_cache
def get_settings():
    """Get core settings."""
    return Settings()
