from db import db


class Image(db.Model):
	__tablename__ = 'images'
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(255), nullable=False, unique=True)
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

	@classmethod
	def create(cls, filename, post_id):
		image = Image(filename=filename, post_id=post_id)
		db.session.add(image)
		db.session.commit()


