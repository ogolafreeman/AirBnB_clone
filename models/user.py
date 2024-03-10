#!/usr/bin/python3

'''class inherent of BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    """User class for representing users."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class."""

        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
