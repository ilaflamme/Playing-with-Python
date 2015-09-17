__author__ = 'ilaflamme'


# ------------------------------------------------------
#
#                  We gonna' code'zez
#
# ------------------------------------------------------


# ------------------------------------------------------
#
# Node class: contains data, a left and right pointer
#
# ------------------------------------------------------

class Node:

    data = None
    left = None
    right = None

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


