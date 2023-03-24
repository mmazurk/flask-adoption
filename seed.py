from models import Pet, db
from app import app

# to run this, just $ python seed.py

db.drop_all()
db.create_all()

p1 = Pet(name = "Wuppers", species = "Doggo", photo_url = "https://cdn.pixabay.com/photo/2017/09/25/13/12/puppy-2785074_960_720.jpg", age = 1, notes = "What a good boy.")
p2 = Pet(name = "Mr. Hoppers", species = "Bunny", photo_url = "https://cdn.pixabay.com/photo/2016/12/04/21/58/rabbit-1882699_960_720.jpg", age = 3, notes = "Likes Carrots.")
p3 = Pet(name = "Cloud", species = "Cat", photo_url = "https://cdn.pixabay.com/photo/2023/03/09/20/02/cat-7840767_960_720.jpg", age = 1, notes = "That's a nice kitty.")
p4 = Pet(name = "Nibblet", species = "Hamster", photo_url = "https://cdn.pixabay.com/photo/2018/02/17/17/50/cute-3160464_960_720.jpg", age = 2, notes = "Ancient by hampster standards.")

pets = [p1, p2, p3, p4]
db.session.add_all(pets)
db.session.commit()
