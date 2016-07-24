from db import db

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False, index=True)
	posts = db.relationship('Post', backref='category')
	img_file = db.Column(db.String(255), nullable=False, index=True)

