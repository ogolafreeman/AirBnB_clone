#!/usr/bin/python3

'''class inherent of BaseModel'''

from models.base_model import BaseModel


class City(BaseModel):
    """City class for representing cities."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class."""

        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
