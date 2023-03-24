
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

@app.route("/")
def show_pets():
    """Show our pets"""

    pets = Pet.query.all()
    return render_template("list-pets.html", pets = pets)

@app.route("/<int:pet_id>/show")
def show_pet(pet_id):
    """Show a specific pet"""
    
    pet = Pet.query.get_or_404(pet_id)
    return render_template("show-pet.html", pet = pet)

@app.route("/<int:pet_id>/edit", methods = ["GET", "POST"])
def edit_pet(pet_id):
    """allows the user to edit a pet"""
    
    form = PetForm()

    if form.validate_on_submit():
        pet = Pet.query.get_or_404(pet_id) 
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else: 
        pet = Pet.query.get_or_404(pet_id)
        form = PetForm(obj=pet)
        return render_template("edit-pet.html", pet = pet, form = form)

@app.route("/add", methods = ["GET", "POST"])
def add_pet():
    """Add new pets"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else: 
        form = PetForm()
        return render_template("add-pet.html", form = form)