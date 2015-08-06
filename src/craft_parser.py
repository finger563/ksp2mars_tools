#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .craft files and extract relevant
information for simulation.
"""

class Model:
    def __init__(self, kind):
        self.kind = kind
        self.children = []
        self.properties = {}

    def addChild(self, child):
        self.children.append(child)

    def addProperty(self, key, value):
        if key:
            self.properties[key] = value

    def __getitem__(self, index):
        return self.properties[index]

object_keys = [
    "PART",
    "EVENTS",
    "ACTIONS",
    "PARTDATA",
    "MODULE",
    "RESOURCE"
    ]

def parse_property(property_str, splitter='='):
    splitted = property_str.split(splitter)
    key, value = None, None
    if len(splitted) > 1:
        key = splitted[0].strip(' ')
        value = splitted[1].strip(' ')
    return key,value

def parse_model(model, model_str):
    submodel_str = ""
    submodel_type = None
    chr_to_strip = '\t'
    for line in model_str:
        sline = line.strip('\t\n')
        if sline in object_keys:
            submodel_type = sline
        elif '{' == sline and submodel_type:
            submodel_str = ''
        elif '}' == sline and submodel_type:
            m = Model(submodel_type)
            parse_model(m, submodel_str)
            model.addChild(m)
            submodel_type = None
        elif submodel_type:
            submodel_str += line
        else:
            k,v = parse_property(sline)
            model.addProperty(k,v)

fname = "/home/jeb/Repositores/ksp2mars_tools/src/kerbalX.craft"

with open(fname) as f:
    root = Model('craft')
    parse_model(root, f)
    print root['ship']
