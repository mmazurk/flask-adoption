
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email

class PetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators = [InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_link = StringField("Photo Link")
    age = IntegerField("Age")
    notes = TextAreaField("Notes on Pet", rows = 2, cols = 20)

