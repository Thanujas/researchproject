import json
from selenium.webdriver.common.by import By
import random
import string

from cffi.backend_ctypes import xrange

from Pages.Homepage import HomePage

def readopenjsonfieldsize_list():
 with open('E:\\researchproject\\sample.json', 'r') as openfile:
   json_object3 = json.load(openfile)
   fielssizesvariable= json_object3['fieldMax_Sizefinal']
   print("xpath variable name-"+fielssizesvariable)
   fieldsizes = fielssizesvariable.split(',')
   print("print sizes values")
   print(len(fieldsizes))
   print(fieldsizes)
   fieldsizesint_list = [int(i) for i in fieldsizes]
   print("Modified list is : " + str(fieldsizesint_list))
   return  fieldsizesint_list

def readopenjsonfieldsizemin_list():
 with open('E:\\researchproject\\sample.json', 'r') as openfile:
   json_object4 = json.load(openfile)
   fielssizesvariablemin= json_object4['fieldMin_Sizefinal']
   print("xpath variable name-"+fielssizesvariablemin)
   fieldsizesmin = fielssizesvariablemin.split(',')
   print("print sizes values")
   print(len(fieldsizesmin))
   print(fieldsizesmin)
   fieldsizesintmin_list = [int(i) for i in fieldsizesmin]
   print("Modified list is : " + str(fieldsizesintmin_list))
   return  fieldsizesintmin_list

class Fieldsizes(object):

 fieldsizelist = readopenjsonfieldsize_list()
 fieldsizelistmin = readopenjsonfieldsizemin_list()
 # # randomstringmaximum = "".join([random.choice(string.ascii_lowercase) for i in xrange()])
 # randomnumbers = "".join([random.choice(string.digits) for i in xrange()])
 # randomcombination = "".join([random.choice(string.punctuation) for i in xrange()])

arraylength1 = len(readopenjsonfieldsize_list())


