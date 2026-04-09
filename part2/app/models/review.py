from app.models.base_model import BaseModel
from app import db

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    