import os
import sys
from flask import Flask
import yaml
from github import Github
import base64

#docker run -t -i -p 5000:5000 assignment1-flask-app

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello from Dockerized Flask App!!"


#Working!
@app.route("/v1/<name>")
def config(name):
	app.config.update(
    yaml.safe_load(open(os.path.join(os.getcwd(), name))))
	return app.config["welcome_message"]

@app.route("/<name>/")
def gitConfig(name):
	file_contents = repo.get_file_contents('/socket-mon.py')
	file_data = file_contents.content
	return base64.b64decode(file_data)


if __name__ == "__main__":
	"""
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	"""
	client = Github('090a38d9a6c345c2aa70a853be86b926926bcfc5')
	user = client.get_user('meenuganesh91')
	repo = user.get_repo('CMPE-273-Lab1')

	file_contents = repo.get_file_contents('/socket-mon.py')
	file_data = file_contents.content
	app.run(debug=True, host='0.0.0.0')
