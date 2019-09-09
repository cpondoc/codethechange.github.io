"""
This file is designed to simplify the process of adding a project narrative to projects.json.
It will take in an HTML file and various project image content, and then add it to the filesystem.
"""
from bs4 import BeautifulSoup
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)
import argparse
parser = argparse.ArgumentParser(description='Add a project to projects.json')
parser.add_argument('project_name', type=str, help="project key as specified in projects.json")
parser.add_argument('html_file', type=str, help='path to the HTML file')
args = parser.parse_args()
soup = None
with open(args.html_file) as fd:
    soup = BeautifulSoup(fd, features="html.parser")
projets_json = {}
# Get the HTML content inside the 'narrative' div
html_str = str(soup.html.body.find(id='narrative')).replace('\n','')[20:-6] 

with open('../src/data/projects.json', 'r') as fd:
    projects_json = json.load(fd)

try:
    project = next(p for p in projects_json if p['name'] == args.project_name)
except StopIteration:
    raise Exception('Make sure that there is a JSON object with "name": "{}" in projects.json'.format(args.project_name))

with open('../src/data/projects.json', 'w') as fd:

    project['narrative'] = html_str
    json.dump(projects_json, fd, sort_keys=True, indent=4)