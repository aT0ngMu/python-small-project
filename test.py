import os
cwd = os.getcwd()
print(cwd)

import reprlib
str_1 = set("svsvdavcafdv")
print(str_1)

str_2 = reprlib.repr(str_1)
print(str_2)

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t,width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate"""
print(textwrap.fill(doc,width=40))

