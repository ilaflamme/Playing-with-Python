__author__ = 'ilaflamme'


# ------------------------------------------------------
#
#                  We gonna' code'zez
#
# ------------------------------------------------------
from Node import Node
class Tree:
    root = None
    outputData = ''
    def __init__(self, root):
        self.root = None

    def addEntry(self, entry):
        if self.root is None:
            self.root = Node(entry)
        else:
            self.addNode(entry, self.root)

    def addNode(self, entry, thisNode):
        if entry < thisNode.data:
            if thisNode.left is None:
                thisNode.left = Node(entry)
            else:
                self.addNode(entry,thisNode.left)
        else:
            if thisNode.right is None:
                thisNode.right = Node(entry)
            else:
                self.addNode(entry,thisNode.right)

    def buildOutput(self, thisNode):
        self.outputData += ("(")
        if thisNode.left is None:
            self.outputData += ("-")
        else:
            self.buildOutput(thisNode.left)

        self.outputData += (",")

        if thisNode.data is None:
            self.outputData += ("-")
        else:
            self.outputData += str(thisNode.data)

        self.outputData += (",")

        if thisNode.right is None:
            self.outputData += ("-")
        else:
            self.buildOutput(thisNode.right)

        self.outputData += (")")

    def printTree(self, thisNode):
        self.buildOutput(thisNode)
        print self.outputData




