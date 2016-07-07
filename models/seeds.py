from db import db
from categories import *

CONST_CATEGORIES = [{name: 'Cars and Trucks',
					 img: 'add image filename for cat here' 
					} 
					
					{name: 'Auto Parts',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Computers',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Electronics',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Video Games',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Camping and Outdoors',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Bicycles',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Sports Equipment',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Animals',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Household Items',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Motorcycles',
					 img: 'add image filename for cat here'
					} 
					
					{name: 'Pizza',
					  img: 'add image filename for cat here'
					}]

for cat in Category.query.all():
	db.session.delete(cat)
db.session.commit()

for obj in CONST_CATEGORIES:
	name = obj['name']
	img = obj['img']
	db.session.add(Category(name=name, img=img))
db.session.commit()