## Node Class (no distance) ##

class Node(object):

    # CONSTRUCTOR 
    def __init__(self, name):

        print("A Classname has been created")

        ### Attributes
        self.name = name       
        self.children = 0
        self.childList = []
        
    ### STRING METHOD - special method that will be called on PRINT  
    def __str__(self):
        report = "\nNode Name:          " + str(self.name) + "\n"
        report = report + "Number of Children: " + str(self.children) + "\n"

        if len(self.childList) > 0:
               report = report + "Has the following Items:\n"
               for i in self.childList:
                   report = report + str(i)
               #report = report + "------"
               
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
c1 = Classname("A")
c2 = Classname("B")
c3 = Classname("C")
c4 = Classname("D")
c1.addChild(c2)
c1.addChild(c3)
c2.addChild(c4)

print(c1)
#print(c2)
#print(c3)



#c1.setName("D")


               


input("\n\nPress the enter key to exit.")
