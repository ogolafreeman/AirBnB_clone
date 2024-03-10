#!/usr/bin/python3

'''class inherent of BaseModel'''

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for representing reviews."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class."""

        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')
