from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository
from app.persistence.repositories.user_repository import UserRepository

from app.persistence.repositories.user_repository import UserRepository
from app.persistence.repositories.place_repository import PlaceRepository
from app.persistence.repositories.review_repository import ReviewRepository
from app.persistence.repositories.amenity_repository import AmenityRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.user_repo = SQLAlchemyRepository(User)

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

        # Logic will be implemented in later tasks

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
    
    def get_all_users(self):
        return self.user_repo.get_all() 

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_amenity(self, amenity_data):
    # Placeholder for logic to create an amenity
        pass

    def get_amenity(self, amenity_id):
    # Placeholder for logic to retrieve an amenity by ID
        pass

    def get_all_amenities(self):
    # Placeholder for logic to retrieve all amenities
        pass

    def update_amenity(self, amenity_id, amenity_data):
    # Placeholder for logic to update an amenity
        pass

    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        pass

    def get_place(self, place_id):
    # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
    # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        pass
