#!/usr/bin/python3

'''class inherent of BaseModel'''

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for representing reviews."""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class."""

        super().__init__(*args, **kwargs)
