from flask import Flask, Blueprint, render_template, flash, redirect, request
from models import *
from flask_mail import Message, Mail
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object('config')

cat = Blueprint('cat', __name__)

mail = Mail(app)






	 	






