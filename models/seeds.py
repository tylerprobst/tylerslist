from db import db
from categories import *

PATH_TO_CAT_PIC = '/assets/categoryPics/'

CONST_CATEGORIES = [{'name': 'Cars and Trucks',
					 'img': PATH_TO_CAT_PIC + 'carsTrucks.JPG'
					}, 
					
					{'name': 'Auto Parts',
					 'img': PATH_TO_CAT_PIC + 'auto-parts.JPG'
					}, 
					
					{'name': 'Computers',
					 'img': PATH_TO_CAT_PIC + 'computers.JPG'
					}, 
					
					{'name': 'Electronics',
					 'img': PATH_TO_CAT_PIC + 'electronics.JPG'
					}, 
					
					{'name': 'Video Games',
					 'img': PATH_TO_CAT_PIC + 'videogames.JPG'
					}, 
					
					{'name': 'Camping and Outdoors',
					 'img': PATH_TO_CAT_PIC + 'camping.JPG'
					}, 
					
					{'name': 'Bicycles',
					 'img': PATH_TO_CAT_PIC + 'bicycle.JPG'
					}, 
					
					{'name': 'Sports Equipment',
					 'img': PATH_TO_CAT_PIC + 'sportsEquipment.JPG'
					}, 
					
					{'name': 'Animals',
					 'img': PATH_TO_CAT_PIC + 'animals.JPG'
					}, 
					
					{'name': 'Household Items',
					 'img': PATH_TO_CAT_PIC + 'householditems.JPG'
					}, 
					
					{'name': 'Motorcycles',
					 'img': PATH_TO_CAT_PIC + 'motorcycle.JPG'
					}, 
					
					{'name': 'Pizza',
					 'img': PATH_TO_CAT_PIC + 'pizza.JPG'
					}]

for cat in Category.query.all():
	db.session.delete(cat)
db.session.commit()

for obj in CONST_CATEGORIES:
	name = obj['name']
	img = obj['img']
	db.session.add(Category(name=name, img_file=img))
db.session.commit()