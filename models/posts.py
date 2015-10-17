from db import db

class Post(db.Model):
	__tablename__= 'posts'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), index=True, nullable=False)
	body = db.Column(db.Text(length=10000), index=True, nullable=False)
	price = db.Column(db.Integer, nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	email = db.Column(db.String(255), nullable=False)
	token = db.Column(db.String(255), nullable=False)
	images = db.relationship('Image', backref='post')

	def update(self, *args, **kwargs):
		try:
			self.title = kwargs['title']
			self.body = kwargs['body']
			self.price = kwargs['price']
			self.email = kwargs['email']
			db.session.add(self)
			db.session.commit()
		except:
			db.session.rollback()

	def delete(self):
		try:	
			db.session.delete(self)
			for image in self.images:	
				db.session.delete(image)

			db.session.commit()
		except:
			db.session.rollback() 
			
	@classmethod
	def create(cls, *args, **kwargs):
		try:
			post = Post(**kwargs)
			db.session.add(post)
			db.session.commit()
		except:
			db.session.rollback()
		return post

	@classmethod
	def querydb(cls, query):
		return db.session.query(cls).filter(cls.title.ilike(query))
