#!/usr/bin/python3
from .base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity for a place (e.g., Wi-Fi, Parking)"""

    def __init__(self, name):
        super().__init__()

        if not name:
            raise ValueError("Amenity name is required")
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or less")

        self.name = name
