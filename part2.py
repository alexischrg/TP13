from exercice1 import *

class BinaryTree:
    def __init__(self,root):
        self.__root = root

    def getroot(self):
        return self.__root


obj = BinaryTree(12)
print(obj.getroot())
n = Node(obj.getroot(),17,5)
print(n.getl())
n1 = Node(n.getl(),6,4)
n2 = Node(n1.getl(),None,3)
print(n2.getr())
n3 = Node(n2.getl(),None,None)
n4 = Node(n1.getr(),None,None)
n5 = Node(n.getr(),19,None)
n6 = Node(n5.getr(),21,18)
n7 = Node(n6.getr(),None,None)
n8 = Node(n6.getl(),None,None)
print(n7.getval())