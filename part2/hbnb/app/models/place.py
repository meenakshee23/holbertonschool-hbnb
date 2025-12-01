#!/usr/bin/python3
from .base_model import BaseModel
from .user import User

class Place(BaseModel):
    """Represents a place owned by a user."""

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        # simple validations required by the instructions
        if not title or len(title) > 100:
            raise ValueError("title is required and must be <= 100 characters")

        if price <= 0:
            raise ValueError("price must be a positive number")

        if latitude < -90 or latitude > 90:
            raise ValueError("latitude must be between -90 and 90")

        if longitude < -180 or longitude > 180:
            raise ValueError("longitude must be between -180 and 180")

        if not isinstance(owner, User):
            raise TypeError("owner must be a User instance")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

        # relationships
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to this place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to this place."""
        self.amenities.append(amenity)
