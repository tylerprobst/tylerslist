from flask import Flask, render_template, Blueprint, session, g	
from models import *
from blueprints import *

application = Flask(__name__)
application.config.from_object('config')

@application.teardown_appcontext
def shutdown_session(exception=None):
        db.session.remove()

@application.route('/')
def home():
	return render_template('home.html')

# test

application.register_blueprint(categories.cat, session=session, g=g)
application.register_blueprint(auth.auth, session=session, g=g)
application.register_blueprint(posts.posts, session=session, g=g)

if __name__ == '__main__':
	application.run()
