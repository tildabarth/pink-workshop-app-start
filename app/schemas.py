import datetime as dt
import typing as t
from enum import Enum

from pydantic import BaseModel


class Color(Enum):
    """Shoe colour enum.

    Colour name corresponds to shoe image in static folder.
    """

    black: str = 'black',
    blue: str = 'blue',
    green: str = 'green',
    mixed: str = 'mixed',
    orange: str = 'orange',
    red: str = 'red',
    yellow: str = 'yellow',


class Status(Enum):
    """Shoe status enum.

    Based on Bulma classes to colour progress bar.
    """

    ok: str = 'success'
    warning: str = 'warning'
    danger: str = 'danger'
    default: str = 'info'


class BaseSchema(BaseModel):
    """Custom base schema."""

    class Config:
        allow_mutation = True
        anystr_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True


class Shoe(BaseSchema):
    """Shoe schema."""
    ...
    #max_distance: int = 500


class Run(BaseSchema):
    """Run schema."""

    @property
    def pace(self) -> str:
        """Get pace as minutes and seconds per km."""
        """
        seconds_per_km = 60**2 / (self.speed * 3.6)
        minutes, seconds = (round(value) for value in divmod(seconds_per_km, 60))
        return f'{minutes}\'{seconds}"'
        """
        return 'X\'Y"'

    @property
    def image_name(self) -> str:
        """Get image name based on time of day."""
        """
        start = self.start
        prefix = 'day'
        if start.hour <= 4 or start.hour > 16:
            prefix = 'evening'
        elif start.hour <= 11:
            prefix = 'morning'
        return f'{prefix}-run.jpg'
        """
        return 'day-run.jpg'

    @property
    def start_time(self) -> str:
        """Get start time as formatted string."""
        #return self.start('%a %b %m @ %H:%M')
        return '[start_time]'
