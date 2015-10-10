from db import db
from categories import *

CONST_CATEGORIES_NAMES = ['Cars and Trucks',
						  'Auto Parts',
						  'Computers',
						  'Electronics',
						  'Video Games',
						  'Camping and Outdoors',
						  'Bicycles',
						  'Sports Equipment',
						  'Animals',
						  'Household Items',
						  'Motorcycles',
						  'Pizza',]

for cat in Category.query.all():
	db.session.delete(cat)
db.session.commit()

for name in CONST_CATEGORIES_NAMES:
	db.session.add(Category(name=name))
db.session.commit()