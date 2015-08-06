#!/usr/bin/python

"""
This program was developed for KSP2Mars
to parse KSP .craft files and extract relevant
information for simulation.
"""
import os,sys,inspect

# Find ANTLR4 python runtime FOR FILESTREAM
antlr4 = os.path.realpath(os.path.abspath
                          (os.path.join
                           (os.path.split
                            (inspect.getfile
                             (inspect.currentframe()
                          )
                         )[0], "Antlr4")
                       ))
if antlr4 not in sys.path:
    sys.path.insert(0, antlr4)
from antlr4 import *

import grammar
from grammar.ksp_craftLexer import ksp_craftLexer
from grammar.ksp_craftParser import ksp_craftParser
from grammar.ksp_craftListener import ksp_craftListener

class Grammar_Field:
    def __init__(self, kind = "", 
                 name = "", 
                 entry_point = None, 
                 exit_point = None, 
                 input_validator = None, 
                 display_name = ""):
        self.kind = kind
        self.name = name
        self.entry_point = entry_point
        self.exit_point = exit_point
        self.input_validator = input_validator
        self.display_name = display_name


# Enter a Model class type while parsing
# E.g. Package, Component, Timer etc.
def create_enterModel(kind):
    def enterModel(self, ctx):
        print "enterModel:: Model Type = " + kind
        new_object = type( kind, (object))()
        new_object.kind = kind
        self.active_objects.append(new_object)
        print "Created New Object: " + str(type(new_object))
    return enterModel

# Exit a Model class type while parsing
def create_exitModel():
    def exitModel(self, ctx):
        child_object = self.active_objects.pop()
        child_object.parent = self.active_objects[-1]
        self.active_objects[-1].add(child_object)
    return exitModel
    
# Enter a Atom type while parsing
# E.g. Name, Value, Period, Unit etc.
def create_enterAtom(kind):
    def enterAtom(self, ctx):
        print "enterAtom:: Property Type = " + kind
        print "enterAtom:: Property Value = " + ctx.getText()
        self.active_objects[-1].properties[kind] = ctx.getText()
    return enterAtom

# Exit a Atom type while parsing
def create_exitAtom():
    def exitAtom(self, ctx):
        pass
    return exitAtom

meta_class_dict = {}

meta_class_dict["part"] = Grammar_Field(
    "object", "part", create_enterModel, create_exitModel, None, "part")

meta_class_dict["attN"] = Grammar_Field(
    "object", "attN", create_enterAtom, create_exitAtom, None, "attN")

# Grammar Metaclass to generate listener functions as part of the builder classes
class Grammar_MetaClass(type):
    # Create new class
    def __new__(cls, name, bases, attrs):
        if name.startswith('None'):
            return None
        for key, value in meta_class_dict.iteritems():
            if value.entry_point:
                attrs['enter' + value.name] = value.entry_point(key)
            if value.exit_point:
                attrs['exit' + value.name] = value.exit_point()
        return super(Grammar_MetaClass, cls).__new__(cls, name, bases, attrs)

    # Initialize new class
    def __init__(self, name, bases, attrs):
        super(Grammar_MetaClass, self).__init__(name, bases, attrs)

class ksp_craft_builder(ksp_craftListener):
    __metaclass__ = Grammar_MetaClass

    def __init__(self):
        self.active_objects = []

def parse_ksp_craft(filename):
    #print "ROSMOD::Parsing File:", filename
    # Read the input model
    model = FileStream(filename)
    # Instantiate the ROSLexer
    lexer = ksp_craftLexer(model)
    # Generate Tokens
    stream = CommonTokenStream(lexer)
    # Instantiate the ROSParser
    parser = ksp_craftParser(stream)
    # Parse from starting point of grammar
    tree = parser.start()
    # Instantiate a Parse Tree Walker
    walker = ParseTreeWalker()
        
    builder = ksp_craft_builder()
    #print "ROSMOD::Reading ROS Workspace:", self.workspace_builder.rml.properties["name"]
    
    # Walk the parse tree
    walker.walk(builder, tree)

parse_ksp_craft("/home/jeb/Repositores/ksp2mars_tools/src/kerbalX.craft")
