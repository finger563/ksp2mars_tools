#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .craft files and extract relevant
information for simulation.
"""

from collections import OrderedDict
import copy

#: These define which delimeters become model objects
object_keys = [
    "PART",
    "EVENTS",
    "ACTIONS",
    "PARTDATA",
    "MODULE",
    "RESOURCE"
    ]

class Model:
    def __init__(self, kind = "none"):
        self.kind = kind
        self.children = []
        self.properties = OrderedDict()

    def addChild(self, child):
        self.children.append(child)

    def addProperty(self, key, value):
        if key:
            self.properties.setdefault(key,[]).append(value)

    def getChildrenByKind(self, kind):
        kids = []
        if kind == self.kind:
            kids.append(self)
        for c in self.children:
            kids.extend(c.getChildrenByKind(kind))
        return kids

    def parse_model(self, model_str, chr_to_strip = ''):
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
                    self.parse_property(line)
            elif submodel_type:
                submodel_str += line + "\n"
                if '{' == sline:
                    num_braces += 1
                elif '}' == sline:
                    num_braces = num_braces - 1
                if num_braces == 0:
                    m = Model(submodel_type)
                    m.parse_model(submodel_str, chr_to_strip)
                    self.addChild(m)
                    submodel_type = None

    def parse_property(self, property_str, splitter='='):
        splitted = property_str.split(splitter)
        if len(splitted) > 1:
            key = splitted[0].strip(' \n\t')
            value = splitted[1].strip(' \n\t')
            self.addProperty(key,value)

    def __getitem__(self, index):
        return self.properties[index]

    def __repr__(self):
        retStr = "{}::\n".format(self.kind)
        for k,v in self.properties.iteritems():
            retStr += "{}:{}\n".format(k,v)
        for c in self.children:
            retStr += "\t{}\n".format(c)
        return retStr

fname = "./kerbalX.craft"

with open(fname) as f:
    root = Model('craft')
    f_str = f.read()
    root.parse_model(f_str, chr_to_strip = '\t ')
    #print root
    parts = root.getChildrenByKind("PART")
    partTree = copy.copy(parts[0])
    print partTree
    
