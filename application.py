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
	categories = Category.query.order_by(Category.name).all()
	return render_template('categories.html', categories=categories)

@application.route('/categories/<path:category_id>')
def category(category_id):
	return render_template('posts.html', posts=Category.query.filter(Category.id==category_id).first().posts)

@application.route('/search')
def search():
	query = request.args.get('query')
	posts = Post.querydb(query)
	return render_template('posts.html', posts=posts)


application.register_blueprint(posts.posts, session=session, g=g)

if __name__ == '__main__':
	application.run()