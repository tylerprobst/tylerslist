from flask import Flask, Blueprint, render_template, redirect, flash, request
from models import * 

auth = Blueprint('auth', __name__)

@auth.route('/verify', methods=['POST'])
def verify():
	if request.method == 'GET':
		print 'hello world'
	elif request.method == 'POST':
		pass