from json import load

with open('static/json/skills.json') as f:
    data = load(f)
skills = data["skills"]
db = data["db"]
pl = data["pl"]
frameworks = data["frameworks"]
print(frameworks)