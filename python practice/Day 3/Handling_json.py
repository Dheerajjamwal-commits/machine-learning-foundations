# This program handles a json which has information about users and thier active status and copies them onto a text file
import json 

with open ("Sample.json",'r') as j:
    data = json.load(j)
with open ("sample_copy.txt",'w') as s:
    for i in data['users']:
        s.writelines(f"{i['name']} with email {i['email']} is {"Active "if i['active'] else "Not Active" }\n")
           