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

from model import Model

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

class Craft(Model):
    def __init__(self, kind = "none"):
        super(Craft, self).__init__(kind)

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
            stage = stages.setdefault(stg,Craft("stage"))
            for resourceType in resourceTypes:
                stage.addProperty(resourceType, self.resources(resourceType))
            for partProp in partProperties:
                pname = self['part'][0].split('_')[0]
                if pname in partDict:
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

def write_csv(fname, stages):
    with open(fname, 'w') as f:
        headerStr = "Stage"
        for prop in partProperties:
            headerStr += ",{}".format(prop)
        for rType in resourceTypes:
            headerStr += ",{}".format(rType)
        headerStr += "\n"
        f.write(headerStr)
        for num,stage in stages.iteritems():
            stgStr = "{}".format(num)
            for prop in partProperties:
                stgStr += ",{}".format(stage[prop])
            for rType in resourceTypes:
                stgStr += ",{}".format(stage[rType])
            stgStr += "\n"
            f.write(stgStr)
    
def main(argv):
    
    fname = "./kerbalX.craft"
    kspdir = "~/SteamLibrary/steamapps/common/Kerbal Space Program"
    outputFileName = "./output.csv"
    if len(argv) == 2:
        fname = argv[1]
    if len(argv) == 3:
        kspdir = argv[1]
        fname = argv[2]
    if len(argv) == 4:
        kspdir = argv[1]
        fname = argv[2]
        outputFileName = argv[3]
    partDict = BuildPartDict(kspdir)
    if not partDict:
        print 'WARNING: no parts found! Check to make sure\n\t{}\nexists!'.format(
            kspdir)

    print "Analyzing craft {}".format(fname)

    with open(fname) as f:
        craft = Craft('craft')
        f_str = f.read()
        craft.parse_model(f_str, chr_to_strip = '\t\r ')
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

    write_csv(outputFileName, stages)

if __name__ == "__main__":
    import sys
    main(sys.argv)
