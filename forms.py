
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email

class PetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators = [InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo Link", render_kw={"size": 75})
    age = IntegerField("Age")
    notes = TextAreaField("Notes on Pet", render_kw={"cols": 30})

