import json
def load_projects():
    projects_json = []
    with open('../src/data/projects.json', 'r') as fd:
        projects_json = json.load(fd)
    return projects_json

def update_projects(projects):
    with open('../src/data/projects.json', 'w') as fd:
        json.dump(projects, fd, sort_keys=True, indent=4)

def get_project(projects, name):
    try:
        project = next(p for p in projects if p['name'] == name)
    except StopIteration:
        raise Exception('Make sure that there is a JSON object with "name": "{}" in projects.json'.format(args.project_name))
    return project