from exercice1 import *

class BinaryTree:
    def __init__(self,root):
        self.__root = root

    def getroot(self):
        return self.__root

    def isRoot(self,node):
        if self.__root == node.getval():
            return True
        else:
            return False

    def size(self, node):
        if node is None:
            return +0
        else :
            return self.size(node.getr()) + self.size(node.getl()) + 1

    """def size(self, node): #codeprof
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def printValues(self, node): #codeprof
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())"""

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return str(node.getval()) + " " + self.printValues(node.getr()) + self.printValues(node.getl())

    def sumValues(self,node):
        if node is None:
            return +0
        else :
            return self.sumValues(node.getr()) + self.sumValues(node.getl()) + node.getval()

    def numberLeaves(self,node):
        if node is None:
            return +0
        elif node.getl() is None and node.getr() is None:
            return 1
        else:
            return self.numberLeaves(node.getr()) + self.numberLeaves(node.getl())

    def numberInternalNodes(self,node):
        #return self.size(node) - self.numberLeaves(node) #méthode plus simple
        if node is None:
            return +0
        elif node.getl() is None and node.getr() is None:
            return +0
        else:
            return 1 + self.numberInternalNodes(node.getr()) + self.numberInternalNodes(node.getl())

    def height(self,node):
        if node is None:
            return - 1
        else:
            return 1 + max(self.height(node.getr()), self.height(node.getl()))

    """def belongs(self, node, val): #verifie si val est une val de l'arbre
        if node == val:
            return True
        elif node.getl() is None and node.getr() is None:
            return False
        else:
            return self.belongs(node.getr(),val) + self.belongs(node.getl(),val)"""

N21 = Node(21, None, None)
N18 = Node(18, None, None)
N3 = Node(3, None, None)
N19 = Node(19, N21, N18)
N4 = Node(4, None, N3)
N6 = Node(6, None, None)
N17 = Node(17, N19, None)
N5 = Node(5, N6, N4)
N12 = Node(12, N17, N5)
Tree = BinaryTree(N12)
print(Tree.size(Tree.getroot())) #9
print(Tree.printValues(Tree.getroot()))
print(Tree.sumValues(Tree.getroot())) #105
print(Tree.numberLeaves(Tree.getroot())) #4
print(Tree.numberInternalNodes(Tree.getroot())) #5
print(Tree.height(Tree.getroot())) #3
#print(Tree.belongs(Tree.getroot(),17)) #True