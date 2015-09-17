__author__ = 'ilaflamme'


# ------------------------------------------------------
#
#                  We gonna' code'zez
#
# ------------------------------------------------------
from Tree import Tree

thisTree = Tree(None)

inputData = [3,5,4,2,8]

for entry in inputData:
    print entry
    thisTree.addEntry(entry)

thisTree.printTree(thisTree.root)