people = [
    {"name": "Cano", "time": "Fluminense"},
    {"name": "Pedro", "time": "Audax"},
    {"name": "Lucumi", "time": "Base"}
]

people.sort(key=lambda person: person["name"])

print(people)