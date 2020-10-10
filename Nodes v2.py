## Node Class (with distance) ##

class Node(object):

    # CONSTRUCTOR 
    def __init__(self, name):

        print("A Classname has been created")

        ### Attributes
        self.name = name       
        self.children = 0
        self.childList = []
        self.distanceList = []
        
    ### STRING METHOD - special method that will be called on PRINT  
    def __str__(self):
        report = "\nNode Name:          " + str(self.name) + "\n"
        report = report + "Number of Children: " + str(self.children) + "\n"

        if len(self.childList) > 0:
               report = report + "Has the following Items:\n"
               for i in self.childList:
                   report = report + str(i)
          
        return report       

    ### OTHER methods  
    def getChildren(self):
        return self.children     

    def getName(self):
        return self.name    

    def setName(self,n):    
        self.name = n

    def addChild(self,item):
        self.childList.append(item)
        self.children = self.children + 1

#MAIN ###################################################

print("\nCreating Classnames.")
c1 = Node("A")
c2 = Node("B")
c3 = Node("C")
c4 = Node("D")
item = [c2,25]
c1.addChild(item)
item = [c3,57]
c1.addChild(item)
item = [c4,21]
c2.addChild(item)

print(c1)
#print(c2)
#print(c3)



#c1.setName("D")


               


input("\n\nPress the enter key to exit.")
