from main import db

class Vaccine(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	vaccine = db.Column(db.String(30))
	date = db.Column(db.String(30))
	next_due = db.Column(db.String(30))