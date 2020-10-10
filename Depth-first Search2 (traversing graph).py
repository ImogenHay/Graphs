### Depth-first Search using Node Class ###

class Node(object):

    # Constructor 
    def __init__(self, name):

        print("A Node has been created")

    # Attributes
        self.name = name       
        self.children_amount = 0
        self.childList = []
        
    # String Method called on print  
    def __str__(self):
        report = "\nNode Name:          " + str(self.name) + "\n"
        report = report + "Number of Children: " + str(self.children_amount) + "\n"
            
        return report       

    # Other Methods  
    def getChildren(self):
        return self.childList

    def getName(self):
        return self.name    

    def setName(self,n):    
        self.name = n

    def addChild(self,item):
        self.childList.append(item)
        self.children_amount = self.children_amount + 1
        

## Main Code ##
print("\nCreating Nodes")
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
j = Node("J")
k = Node("K")
a.addChild(c)
a.addChild(b)
b.addChild(k)
c.addChild(f)
c.addChild(d)
d.addChild(g)
d.addChild(h)
d.addChild(e)
f.addChild(j)
f.addChild(g)
j.addChild(h)
h.addChild(d)
total_children = 12


nodes = [a] #starts at beginning 
for i in range (0,total_children): #repeats for all children
    children = nodes[i].getChildren() #gets children of current node 
    for x in range (0,len(children)): #repeats for all of parents children
        nodes.insert((nodes.index(nodes[i]))+(x+1),children[x]) #inserts children after parent     
children = b.getChildren() #repats for second branch
for x in range (0,len(children)):
        nodes.append(children[x])

#Remove repeats in list
nodes2 = []
for i in nodes:
    if i not in nodes2:
        nodes2.append(i)

#Print nodes in corrent order
for x in range (0,len(nodes2)):
    print(nodes2[x])


        




input("\n\nPress the enter key to exit.")
