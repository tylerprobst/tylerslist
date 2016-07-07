from flask import Flask, Blueprint, request, session, send_from_directory, render_template, flash, redirect
from models import *
import bcrypt
from flask_mail import Mail, Message
from werkzeug import secure_filename
import os, random, string
from boto_conn import bucket

app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)

posts = Blueprint('posts', __name__)

@posts.route('/posts', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('posts.html', posts=Post.query.all())
	elif request.method == 'POST':
		pass


@posts.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create.html', categories=Category.query.all())
	elif request.method == 'POST':
		title = request.form.get('title')
		body = request.form.get('body')
		category_id = request.form.get('category_id')
		email = request.form.get('email')
		price = request.form.get('price')
		token = bcrypt.gensalt()
		if title and body and email and price:
			post = Post.create(title=title, body=body, category_id=category_id, email=email, price=price, token=token)
			for img_file in request.files.getlist('file[]'):
				filename = 'None'
				if img_file:
					filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(26)) + ".jpeg"
					if filename:
						# img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
						key = bucket.new_key(filename)
						key.set_contents_from_string(img_file.read())
						key.set_canned_acl('public-read')
						image = Image.create(filename=filename, post_id=post.id)
			link = 'http://tylerslist.elasticbeanstalk.com/edit/{1}?token={0}'.format(token, post.id)
			msg = Message('Edit post email', sender='tprobstcoding@gmail.com', recipients=[email])
			msg.body = "Use this link to edit your post: " + link
			mail.send(msg)
			flash('Post was successfully created, please check your email for an editing link.')
			return redirect('/')
		else:
			flash('please fill out the required fields')
			return render_template('create.html')

@posts.route('/post/delete/<path:post_id>')
def delete(post_id):
	post = Post.query.filter(Post.id==post_id).first()
	post.delete()
	flash('Post Deleted')
	return redirect('/')

@posts.route('/posts/<path:post_id>')
def post(post_id):
	post = Post.query.filter(Post.id==post_id).first()
	images = post.images
	return render_template('post.html', post=post, images=images)


@posts.route('/edit/<path:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
	if request.method == 'GET':
		token = request.args.get('token')
		post = Post.query.filter(Post.id==post_id).first()
		category = Category.query.filter(Category.id==post.category_id).first()
		if token != post.token:
			flash('Please use a valid email link!')
			return render_template('home.html')
		return render_template('edit_post.html', post=post, category_name=category.name)
	elif request.method == 'POST':
		post = Post.query.filter(Post.id==post_id).first()
		title = request.form.get('title')
		body = request.form.get('body')
		price = request.form.get('price')
		email = request.form.get('email')
		img_file = request.files.get('file')
		filename = 'None'
		if img_file:
			if img_file.filename != post.img_filename:
				filename = secure_filename(img_file.filename) 			#randomize the filename using BCRYPT
				img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				image = Image.create(filename=filename, post_id=post.id)
		post.update(title=title, body=body, email=email, price=price, filename=filename)
		flash('Your post was updated')
		return redirect('/posts')


@posts.route('/uploads', methods=['POST'])
def upload():
	img_file = request.files.get('file')
	filename = secure_filename(img_file.filename) 		
	img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return '<img src="/uploads/{0}" />'.format(filename)

@posts.route('/assets', methods=['POST'])
def asset():
	img_file = request.files.get('file')
	filename = secure_filename(img_file.filename) 		
	img_file.save(os.path.join(app.config['ASSET_FOLDER'], filename))
	return '<img src="/assets/{0}" />'.format(filename)


@posts.route('/assets/<path:filename>')
def assets(filename):
	return send_from_directory('assets', filename)

@posts.route('/uploads/<path:filename>')
def uploads(filename):
	return send_from_directory('uploads', filename)	
