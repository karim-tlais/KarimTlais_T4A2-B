from main import db

class Profile(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	pet_name = db.Column(db.String(30))
	pet_breed = db.Column(db.String(30))
	pet_dob = db.Column(db.String(30))
	pet_sex = db.Column(db.String(30))