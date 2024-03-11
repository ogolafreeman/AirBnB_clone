#!/usr/bin/python3

'''class inherent of BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    """User class for representing users."""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class."""
        super().__init__(*args, **kwargs)
