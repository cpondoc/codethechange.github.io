import pandas as pd
import pprint
from math import isnan
import json
pp = pprint.PrettyPrinter(indent=4)
obj = pd.read_csv('./profiles.csv')
projects = {}
peeps = {}
with open('/Users/drewgregory/Documents/CTC/website/src/data/people.json', 'r') as fp:
    peeps = json.load(fp)
for i in range(12, len(obj['Timestamp'])):
    key = obj['Name'][i].lower().replace(" ", "")
    peeps[key] = {}
    peeps[key]['name'] = obj['Name'][i]
    peeps[key]['role'] = obj['Role'][i]
    peeps[key]['role'] = obj['Role'][i]
    peeps[key]['imageSrc'] = "./assets/" + obj['Profile Picture URI Name'][i]
    peeps[key]['links'] = {}
    for link in ['GitHub Link','Email','LinkedIn Link']:
        if str(obj[link][i]) != "nan":
            peeps[key]['links'][link.lower().replace(" link", "")] = obj[link][i]
    projectName = obj['Projects (with CTC)'][i]
    if str(projectName) != "nan":
        projectName = projectName.lower().replace(" ", "")
        if projectName not in projects:
            projects[projectName] = []
        projects[projectName].append(key)

with open('people.json', 'w') as fp:
    json.dump(peeps, fp, sort_keys=True, indent=4)

with open('projects.json', 'w') as fp:
    json.dump(projects, fp, sort_keys=True, indent=4)
