
import base64
import sys
from flask import Flask
from github import Github
import yaml
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello from Dockerized Flask App!!"

@app.route("/v1/<name>")
def gitConfig(name):
	try:
		if name.endswith(".yml"):
			file_contents = repo.get_file_contents('/' + name)
			file_data = file_contents.content
			return base64.b64decode(file_data)
		elif name.endswith(".json"):
			name = name.replace(".json", ".yml")
			file_contents = repo.get_file_contents('/' + name)
			file_data = json.dumps(yaml.load(base64.b64decode(file_contents.content)), sort_keys=False, indent=2)
			return file_data
		else:
			return "Incorrect file format!!\nFile should be in yml or json format.\n"
	
	except:
		return "File not found in repository!!\n"
	
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Github url needed to process requests"
		exit()
	else:
		repo_url = str(sys.argv[1])
		repo_url = repo_url.split("/")
		try:
			username = repo_url[repo_url.index("github.com")+1]
			repo_name = repo_url[repo_url.index(username)+1]
			client = Github("meenuganesh91", "AmenRedWim3")
			user = client.get_user(username)
			repo = user.get_repo(repo_name)
			app.run(debug=True, host='0.0.0.0')
		except:
			print "Github url needed to process requests"
			exit()
