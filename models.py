
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """This sets up a connection between a Flask application and a database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """This object represents a Pet in our adoption app"""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    name = db.Column(db.String(20),
                            nullable=False)
    species = db.Column(db.String(20),
                            nullable=False)
    photo_url = db.Column(db.String(200),
                            default="https://cdn.pixabay.com/photo/2017/09/25/13/12/puppy-2785074_960_720.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.String(600))
    available = db.Column(db.Boolean, default=True)
