"""
This file is designed to simplify the process of adding a project narrative to projects.json.
It will take in an HTML file and various project image content, and then add it to the filesystem.
"""
from bs4 import BeautifulSoup
import load_write_projects
import argparse
parser = argparse.ArgumentParser(description='Add a project to projects.json')
parser.add_argument('project_name', type=str, help="project key as specified in projects.json")
parser.add_argument('html_file', type=str, help='path to the HTML file')
args = parser.parse_args()
soup = None
with open(args.html_file) as fd:
    soup = BeautifulSoup(fd, features="html.parser")
projects_json = load_write_projects.load_projects()
# Get the HTML content inside the 'narrative' div
html_str = str(soup.html.body.find(id='narrative')).replace('\n','')[20:-6] 
project = load_write_projects.get_project(projects_json, args.project_name)
project['narrative'] = html_str
load_write_projects.update_projects(projects_json)
