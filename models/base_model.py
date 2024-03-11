#!/usr/bin/python3
'''module base_model'''


from datetime import datetime
import uuid
import models


class BaseModel():
    '''class BaseModel'''
    def __init__(self, *args, **kwarg):
        """
        Constructor for BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty:
            - Each key of this dictionary is an attribute name.
            - Each value of this dictionary is the value
            of this attribute name.

            Note:
                - '__class__' from kwargs is the only
                one that should not be added as an attribute.

            Warning:
                - 'created_at' and 'updated_at' are strings
                in this dictionary, but inside your BaseModel
                instance is working with datetime object.
                  You have to convert these strings into datetime object.
                  Tip: You know the string format of these datetime.

        Otherwise:
            - Create id, created_at, and updated_at as
            you did previously (new instance).
        """
        if kwarg:
            for key, value in kwarg.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel
            instance in the format [<class name>] (<self.id>) <self.__dict__>.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute 'updated_at'
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Returns:
            dict: A dictionary representation of the
            instance with all keys/values of __dict__.
                  Keys:
                    - __class__: Class name of the object.
                    - created_at: Creation datetime string in ISO format.
                    - updated_at: Update datetime string in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
