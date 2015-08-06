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
        self.parent = None
        self.children = []
        self.properties = OrderedDict()

    def addChild(self, child):
        child.parent = self
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

    def resolve_attN(self, parts):
        key = "attN"
        if key not in self.properties:
            return
        vals = self.properties[key]
        refVals = {}
        for val in vals:
            pos = val.split(',')[0]
            name = val.split(',')[1]
            for part in parts:
                if name in part["part"]:
                    refVals[pos] = part
                    break
        self.properties[key] = refVals

    def resolve_link(self, parts):
        key = "link"
        if key not in self.properties:
            return
        vals = self.properties[key]
        refVals = []
        for val in vals:
            for part in parts:
                if val in part["part"]:
                    refVals.append(part)
                    break
        self.properties[key] = refVals

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

    def toStr(self, prefix='', printProps = True, printChildren = False):
        retStr = "{}{}::\n".format(prefix, self.kind)
        if printProps:
            for k,v in self.properties.iteritems():
                retStr += "{}\t{}:{}\n".format(prefix,k,v)
        if printChildren:
            for c in self.children:
                retStr += "{}\n".format(c.toStr(prefix+'\t', printProps, printChildren))
        return retStr

fname = "./kerbalX.craft"

with open(fname) as f:
    craft = Model('craft')
    f_str = f.read()
    craft.parse_model(f_str, chr_to_strip = '\t ')
    #print root
    parts = craft.getChildrenByKind("PART")
    for p in parts:
        p.resolve_attN(parts)
        p.resolve_link(parts)
    rootPart = parts[0]
    print rootPart.toStr('',True,True)
