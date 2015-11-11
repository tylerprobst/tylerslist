import boto
import boto.s3.connection
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

conn = boto.connect_s3(
	aws_access_key_id     = app.config['AWS_ACCESS_KEY'],
	aws_secret_access_key = app.config['AWS_SECRET_KEY'],
	host=app.config['S3_HOST_NAME'])

bucket = conn.get_bucket(app.config['S3_BUCKET_NAME'])
