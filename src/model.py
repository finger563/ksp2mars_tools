#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .part files and extract relevant
information for simulation.
"""

from collections import OrderedDict

class Model(object):
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

    def parse_model(self, model_str, chr_to_strip = ''):
        submodel_str = ""
        submodel_type = None
        prevLine = None
        num_braces = 0
        for line in model_str.split('\n'):
            sline = line.strip(chr_to_strip)
            if not submodel_type:
                if '{' == sline and prevLine:
                    num_braces += 1
                    submodel_str += line + "\n"
                    submodel_type = prevLine.strip(chr_to_strip)
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
                    m = self.__class__(submodel_type)
                    m.parse_model(submodel_str, chr_to_strip)
                    self.addChild(m)
                    submodel_type = None
            prevLine = line

    def parse_property(self, property_str, splitter='='):
        splitted = property_str.split(splitter)
        if len(splitted) > 1:
            key = splitted[0].strip(' \n\t')
            value = splitted[1].strip(' \n\t')
            self.addProperty(key,value)

    def __getitem__(self, index):
        return self.properties[index]

    def __setitem__(self, index, val):
        self.properties[index] = val

    def toStr(self, prefix='', printProps = True, printChildren = False):
        retStr = "{}{}::\n".format(prefix, self.kind)
        if printProps:
            for k,v in self.properties.iteritems():
                retStr += "{}\t{}:{}\n".format(prefix,k,v)
        if printChildren:
            retStr += "{}children:\n".format(prefix)
            for c in [x for x in self.children if x.kind == "PART"]:
                retStr += "{}\n".format(c.toStr(prefix+' ', printProps, printChildren))
        return retStr

