#HW: interface for adding multiple images --- ask for assistance
#hw: SEARCH!: construct query with entered search, seach titles and bodys of things in database, look for search under sqlalchemy


from flask import Flask, render_template, Blueprint, session, g	
from models import *
from blueprints import *

app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def home():
	return render_template('home.html')

app.register_blueprint(categories.cat, session=session, g=g)
app.register_blueprint(auth.auth, session=session, g=g)
app.register_blueprint(posts.posts, session=session, g=g)

if __name__ == '__main__':
	app.run()
