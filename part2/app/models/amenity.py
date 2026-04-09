from app.models.base_model import BaseModel
from app import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(100), nullable=False)