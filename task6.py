import re
# re.findall()
from re import findall
from re import *

# findall()
from time import sleep

import xml.etree.ElementTree as et
#
# import test_module
#
# print(test_module.a)
#
# test_module.add()
# print(test_module.a)

import test.test_package

from test import test_package
from test.test_package import a

print(test.test_package.a)
print(test_package.a)
print(a)


import sys
print(sys.path)
print(sys.argv)

# a = sys.argv[1]
# print(a)

import os


a = open('test_module.py')
print(a.read())