"""
Add images to the project listing by merely listing the relative file paths.
This script:
1) Moves the image to the public/assets folder with a unique name
2) Adds the image to the project listing definition in projects.json.
"""
import os
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)
import argparse
import shutil
import load_write_projects
parser = argparse.ArgumentParser(description='Add images to projects.json')
parser.add_argument('project_name', type=str, help="project name field as specified in projects.json")
parser.add_argument('image_file', type=str, help='path to the image file')
parser.add_argument('caption', type=str, help='caption to the image')
args = parser.parse_args()
dirpath = os.getcwd()
shutil.move(args.image_file, dirpath + '/../public/assets/')
projects = load_write_projects.load_projects()
project = load_write_projects.get_project(projects, args.project_name)
if 'assets' not in project:
    project['assets'] = []
project['assets'].append({
    'caption': args.caption,
    'src': './assets/{}'.format(args.image_file.split('/')[-1]),
})
load_write_projects.update_projects(projects)
