#!/usr/bin/python3
"""defines all common attributes/methods for other classes:
    """

import datetime
import uuid


class BaseModel:
    """defines all common attributes/methods for other classes:
    """

    def __init__(self) -> None:
        """Initialization of Public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self) -> str:
        """print: [<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: string representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance

        Returns:
            dict: all keys/values of the instance
        """
        d1 = self.__dict__
        d1["__class__"] = self.__class__.__name__
        # created_at and updated_at must be converted to string object in ISO
        # format isoformat()
        d1['updated_at'] = d1['updated_at'].isoformat()
        d1['created_at'] = d1['created_at'].isoformat()
        return d1
