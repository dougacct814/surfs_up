# Import flask
from flask import Flask
app = Flask(__name__)

# Define starting point or root
@app.route('/')
def hello_world():
	return 'Hello world'

	