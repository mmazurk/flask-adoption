
from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import PetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push() 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all() 

@app.route("/", methods = ["GET", "POST"])
def add_pet():
    """list existing pets or add new pets"""

    add_form = PetForm()

    if add_form.validate_on_submit():
        name = add_form.name.data
        species = add_form.species.data
        pet = Pet(name = name, species = species)
        db.session.add(pet)
        db.session.commit()
        return redirect('pets.html')
    else:
        return render_template("list-pets.html", form = add_form)

@app.route("/<int:pet_id>/show")
def show_pet(pet_id):
    """Show a specific pet"""
    
    pet = Pet.query.get_or_404(pet_id)
    return render_template("show-pet.html", pet = pet)

@app.route("/pets/<int:pet_id>/edit", methods = ["GET", "POST"])
def edit_pet(pet_id):
    """allows the user to edit a pet"""
    
    edit_form = PetForm()
    pet = Pet.query.get_or_404(pet_id)
    edit_form = PetForm(obj=pet)

    return render_template("edit_employee_form.html", form = edit_form)