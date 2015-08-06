#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .craft files and extract relevant
information for simulation.
"""

from collections import OrderedDict

class Model:
    def __init__(self, kind = "none"):
        self.kind = kind
        self.children = []
        self.properties = OrderedDict()

    def addChild(self, child):
        self.children.append(child)

    def addProperty(self, key, value):
        if key:
            self.properties[key] = value

    def __getitem__(self, index):
        return self.properties[index]

    def __repr__(self):
        retStr = "{}::\n".format(self.kind)
        for k,v in self.properties.iteritems():
            retStr += "{}:{}\n".format(k,v)
        for c in self.children:
            retStr += "\t{}\n".format(c)
        return retStr

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
        key = splitted[0].strip(' \n')
        value = splitted[1].strip(' \n')
    return key,value

def parse_model(model, model_str, chr_to_strip = ''):
    submodel_str = ""
    submodel_type = None
    num_braces = 0
    for line in model_str.split('\n'):
        sline = line.strip(chr_to_strip)
        if not submodel_type:
            if sline in object_keys:
                submodel_type = sline
                submodel_str = ''
            elif '=' in sline:
                k,v = parse_property(line)
                model.addProperty(k,v)
        elif submodel_type:
            submodel_str += line + "\n"
            if '{' == sline:
                num_braces += 1
            elif '}' == sline:
                num_braces = num_braces - 1
                if num_braces == 0:
                    m = Model(submodel_type)
                    parse_model(m, submodel_str, chr_to_strip)
                    model.addChild(m)
                    submodel_type = None

fname = "./kerbalX.craft"

with open(fname) as f:
    root = Model('craft')
    f_str = f.read()
    parse_model(root, f_str, chr_to_strip = '\t ')
    print root
