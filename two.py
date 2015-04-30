 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml
import types

def recurse(dict, v):
    for key in dict:
        if key == 'death':
            if dict[key] == None:
                print dict['birth'], " - ", dict['name']

        if type(dict[key]) is types.DictType:
            recurse(dict[key], v+1)

        elif type(dict[key]) == types.ListType:
            for i in range(len(dict[key])):
                recurse(dict[key][i], v+1)


with open("bernadotte.yaml") as f:
    family = yaml.load(f)

recurse(family, 0)
