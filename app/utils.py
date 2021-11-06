"""App utility functions."""

import re


def strip_url_scheme(url: str) -> str:
    """Remove scheme (protocol) from URL."""
    pattern = re.compile('^https?:')
    return pattern.sub('', url)
