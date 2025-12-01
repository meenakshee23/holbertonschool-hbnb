#!/usr/bin/python3
from .base_model import BaseModel
from .user import User
from .place import Place

class Review(BaseModel):
    """Represents a review written by a user for a place."""

    def __init__(self, text, rating, place, user):
        super().__init__()

        if not text:
            raise ValueError("Review text is required")

        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("rating must be an integer between 1 and 5")

        if not isinstance(place, Place):
            raise TypeError("place must be a Place instance")

        if not isinstance(user, User):
            raise TypeError("user must be a User instance")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
