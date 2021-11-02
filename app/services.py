import typing as t

import requests

from settings import get_settings
from app.schemas import Run, Shoe


settings = get_settings()


def get_runs() -> t.List[Run]:
    """Get list of runs from API."""
    return []
