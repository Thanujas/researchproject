import json
from collections import defaultdict

from selenium.webdriver.common.by import By

from Pages.Homepage import HomePage

def readopenjsondatainput_list():
 with open('E:\\researchproject\\sample.json', 'r') as openfile:
   json_object4 = json.load(openfile)
   fieldallowablevariable= json_object4['fieldAllowable_datatypesfinal']
   print("xpath variable name-"+fieldallowablevariable)
   allowabledatatypes = fieldallowablevariable.split(',')
   print("print allowable data types values")
   print(len(allowabledatatypes))
   print(allowabledatatypes)
   return  allowabledatatypes

def readopenjsondatainputnon_list():
 with open('E:\\researchproject\\sample.json', 'r') as openfile:
   json_object4 = json.load(openfile)
   fieldnonallowablevariable= json_object4['fieldNonAllowable_datatypesfinal']
   print("xpath variable name-"+fieldnonallowablevariable)
   nonallowabledatatypes = fieldnonallowablevariable.split(',')
   print("print allowable data types values")
   print(len(nonallowabledatatypes))
   print(nonallowabledatatypes)
   return  nonallowabledatatypes

class Charachterdatatypes(object):

 fieldallowablelist = readopenjsondatainput_list()
 fieldnonallowablelist = readopenjsondatainputnon_list()

arraylength1 = len(readopenjsondatainput_list())


