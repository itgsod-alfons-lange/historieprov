 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml
import types



def recurse(dict, people):
    for key in dict:
        if key == 'death':
            if not dict['death'] == None:
                thisage = dict['death'] - dict['birth']
                people.append({'name':dict['name'], 'age':thisage})
                print thisage, "--", dict['name']

        if type(dict[key]) is types.DictType:
            recurse(dict[key], people)

        elif type(dict[key]) == types.ListType:
            for i in range(len(dict[key])):
                recurse(dict[key][i], people)
    return people

with open("bernadotte.yaml") as f:
    family = yaml.load(f)
people = recurse(family, [])
print "Result is: " + str(people)


for i in range(len(people)-1):
    for j in range(len(people)-(i+1)):
        if people[j]['age'] > people[j+1]['age']:
            people[j],people[j+1] = people[j+1],people[j]

print "\n"*5
print "The oldest is : ", people[len(people)-1]
