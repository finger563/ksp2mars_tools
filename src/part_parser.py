#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .part files and extract relevant
information for simulation.
"""

from collections import OrderedDict
import copy
import operator
import glob
import os
import fnmatch

from model import Model

fuelDensity = 0.005  # 5 kg / unit of fuel (both liquid fuel and oxidizer)

class Part(Model):
    def __init__(self, kind = "none"):
        super(Part, self).__init__(kind)

    def getMass(self):
        mass = 0
        if 'mass' in self.properties:
            mass = float(self['mass'][0].split(' ')[0])
        self['mass'] = mass
        return mass

    def getDryMass(self):
        mass = self['mass']
        self['dryMass'] = mass
        return mass

    def getWetMass(self):
        mass = self['mass']
        if mass:
            for m in self.getChildrenByKind('RESOURCE'):
                if 'LiquidFuel' in m['name'] or 'Oxidizer' in m['name']:
                    mass += float(m['amount'][0].split('\t')[0]) * fuelDensity
        self['wetMass'] = mass
        return mass

    def getDrag(self):
        drag = 0
        if 'maximum_drag' in self.properties:
            drag = float(self['maximum_drag'][0])
        self['drag'] = drag
        return drag

    def getAngularDrag(self):
        drag = 0
        if 'angularDrag' in self.properties:
            drag = float(self['angularDrag'][0])
        self['angular_drag'] = drag
        return drag

    def getISPKeys(self):
        keys = None
        for m in self.getChildrenByKind("MODULE"):
            if "ModuleEngines" in m['name'][0]:
                atmoCurve = m.getChildrenByKind('atmosphereCurve')[0]
                keys = atmoCurve['key']
        return keys

    def getISP_Vac(self):
        isp = 0
        keys = self.getISPKeys()
        if keys:
            for key in keys:
                if '0 ' in key:
                    isp = key.split(' ')[1]
        self['isp_vac'] = isp
        return isp

    def getISP_Srf(self):
        isp = 0
        keys = self.getISPKeys()
        if keys:
            for key in keys:
                if '1 ' in key:
                    isp = key.split(' ')[1]
        self['isp_srf'] = isp
        return isp

    def getThrust(self):
        thrust = 0
        for m in self.getChildrenByKind("MODULE"):
            if "ModuleEngines" in m['name'][0]:
                thrust = float(m['maxThrust'][0])
        self['thrust'] = thrust
        return thrust

def BuildPartDict(kspdir = "~/SteamLibrary/steamapps/common/Kerbal Space Program",
                  subDir = "GameData"):
    print "Parsing parts in KSP install: {}".format(kspdir)
    kspdir = os.path.expanduser(kspdir)
    partDir = os.path.join(kspdir,subDir)

    # GET ALL PARTS WHICH FOLLOW PATTERN: GameData/*/Parts/*/*.cfg
    partFileNames = []
    for root, dirnames, filenames in os.walk(partDir):
        for dirname in fnmatch.filter(dirnames, 'Parts'):
            for r, d, f in os.walk(os.path.join(root,dirname)):
                for filename in fnmatch.filter(f, '*.cfg'):
                    partFileNames.append(os.path.join(r, filename))

    partDict = {}

    for partFileName in partFileNames:
        with open(partFileName) as f:
            part = Part('base')
            f_str = f.read()
            part.parse_model(f_str, chr_to_strip = '\t\r ')
            parts = part.getChildrenByKind("PART")
            realPart = None
            if 'name' in part.properties:
                realPart = part
            elif parts:
                realPart = parts[0]

            if realPart:
                realPart.getMass()
                realPart.getDryMass()
                realPart.getWetMass()
                realPart.getISP_Vac()
                realPart.getISP_Srf()
                realPart.getDrag()
                realPart.getThrust()
                partDict[realPart['name'][0]] = realPart
    return partDict

def main(argv):
    kspdir = "~/SteamLibrary/steamapps/common/Kerbal\ Space\ Program/"
    if len(argv) > 1:
        kspdir = argv[1]

    partDict = BuildPartDict(kspdir)
    print partDict
    
if __name__ == "__main__":
    import sys
    main(sys.argv)
