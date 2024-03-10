#!/usr/bin/python3

'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for representing amenities."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the class."""

        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
