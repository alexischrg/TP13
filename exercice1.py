class Node:
    def __init__(self,val,r=None,l=None):
        self.__val = val
        self.__right = r
        self.__left = l

    #def setval(self,v):
        #self.__val = v
    def setr(self, r):
        self.__right = r
    def setl(self, l):
        self.__left = l

    def getval(self):
        return self.__val
    def getr(self):
        return self.__right
    def getl(self):
        return self.__left

#n = Node(12,17,5)
#print(n.getr())
#n.setl(7)
#print(n.getl())
