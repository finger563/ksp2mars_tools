#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .craft files and extract relevant
information for simulation.
"""

from collections import OrderedDict
import copy
import operator

from part_parser import BuildPartDict

#TODO:
# USE SYM FIELD TO DETERMINE SYMMETRY AND EVEN BETTER STAGING

#: These define which delimeters become model objects
object_keys = [
    "PART",
    "EVENTS",
    "ACTIONS",
    "PARTDATA",
    "MODULE",
    "RESOURCE"
]

resourceTypes = [
    'MonoPropellant',
    'ElectricCharge',
    'LiquidFuel',
    'Oxidizer',
]
partProperties = [
    'isp_vac',
    'isp_srf',
    'drag',
    'wetMass',
    'dryMass',
    'thrust',
]

class Model:
    def __init__(self, kind = "none"):
        self.kind = kind
        self.parent = None
        self.children = []
        self.properties = OrderedDict()

    def stage(self):
        if 'istg' in self.properties:
            return self['istg'][0]
        else:
            return -1

    def resources(self,key):
        res = 0
        for c in [x for x in self.children if x.kind == "RESOURCE"]:
            if key in c["name"]:
                res += int(c["amount"][0])
        return res

    def sumResources(self, key):
        if key in self.properties:
            sum = 0
            for num in self[key]:
                sum += float(num)
            self[key] = sum

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

    def buildPartTree(self):
        keys = ["link"]
        for key in keys:
            if key in self.properties:
                for part in self.properties[key]:
                    if part != self.parent:
                        self.addChild(part)
                        part.buildPartTree()

    def buildStageInfo(self, stages, partDict):
        stg = self.stage()
        if stg > 0:
            stage = stages.setdefault(stg,Model("stage"))
            for resourceType in resourceTypes:
                stage.addProperty(resourceType, self.resources(resourceType))
            for partProp in partProperties:
                pname = self['part'][0].split('_')[0]
                if pname in partDict:
                    print partProp, partDict[pname][partProp]
                    stage.addProperty(partProp, partDict[pname][partProp])
        for c in self.children:
            c.buildStageInfo(stages, partDict)

    def resolve_refs(self, key, parts):
        if key not in self.properties:
            return
        vals = self.properties[key]
        refVals = []
        for val in vals:
            if len(val.split(',')) > 1:
                val = val.split(',')[1]
            for part in parts:
                if val in part["part"]:
                    refVals.append(part)
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

    def __setitem__(self, index, val):
        self.properties[index] = val

    def toStr(self, prefix='', printProps = True, printChildren = False):
        retStr = "{}{}::\n".format(prefix, self.kind)
        retStr += "{}stage : {}\n".format(prefix, self["istg"][0])
        if printProps:
            for k,v in self.properties.iteritems():
                retStr += "{}\t{}:{}\n".format(prefix,k,v)
        if printChildren:
            for c in [x for x in self.children if x.kind == "PART"]:
                retStr += "{}\n".format(c.toStr(prefix+' ', printProps, printChildren))
        return retStr

def main(argv):
    
    fname = "./kerbalX.craft"
    kspdir = "~/SteamLibrary/steamapps/common/Kerbal Space Program"
    if len(argv) == 2:
        fname = argv[1]
    if len(argv) == 3:
        kspdir = argv[1]
        fname = argv[2]
    partDict = BuildPartDict(kspdir)

    print "Analyzing craft {}".format(fname)

    with open(fname) as f:
        craft = Model('craft')
        f_str = f.read()
        craft.parse_model(f_str, chr_to_strip = '\t ')
        parts = craft.getChildrenByKind("PART")
        for p in parts:
            p.resolve_refs("srfN",parts)
            p.resolve_refs("attN",parts)
            p.resolve_refs("link",parts)
        rootPart = parts[0]
        rootPart.buildPartTree()
        #print rootPart.toStr('',True,True)
        
        stages = OrderedDict()
        rootPart.buildStageInfo(stages, partDict)

        # CONVERT FROM INVERSE STAGE NUMBER TO STAGE NUMBER
        newStages = OrderedDict()
        stages = sorted(stages.items(), key=operator.itemgetter(0))
        highest = stages[-1][0]
        for num, stage in stages:
            newStages[int(highest)-int(num)] = stage
        stages = newStages

        for num, stage in stages.iteritems():
            print "Stage {}:".format(num)
            for rType in resourceTypes:
                stage.sumResources(rType)
                print "\t{}: {}".format(rType, stage[rType])
            for pProp in partProperties:
                stage.sumResources(pProp)
                print "\t{}: {}".format(pProp, stage[pProp])

if __name__ == "__main__":
    import sys
    main(sys.argv)
