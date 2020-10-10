### Breadth-first Search using Node Class ###

class Node(object):

    # Constructor 
    def __init__(self, name): 

        print("A Node has been created")

    # Attributes
        self.name = name #name of the object       
        self.children_amount = 0 #number of children the class has
        self.childList = [] #list of all of objects children
        
    # String Method called on print  
    def __str__(self):
        report = "\nNode Name:          " + str(self.name) + "\n"
        report = report + "Number of Children: " + str(self.children_amount) + "\n"          
        return report       

    # Other Methods  
    def getChildren(self):
        return self.childList #returns all the objects children

    def getName(self):
        return self.name #return the name of the object  

    def setName(self,n):    
        self.name = n #set the name of the object

    def addChild(self,item):
        self.childList.append(item) #appends the new chidl to the list of children
        self.children_amount = self.children_amount + 1 #increases child counter by 1 each time one added

## Main Code ##
print("\nCreating Nodes")
a = Node("A") #creates all the nodes
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
a.addChild(b) #links the nodes so they are a graph
a.addChild(c)
a.addChild(d)
c.addChild(e)
d.addChild(f)
e.addChild(f)

print("\nFirst Row: ") 
current_nodes = [a] 
print(current_nodes[0]) #prints 'a' which is at top of graph

print("\nSecond Row: ")
current_nodes = current_nodes[0].getChildren()#appends a's children to the list
if len(current_nodes) > 0:
    for i in current_nodes: #prints a's children
        print(str(i))

print("\nThird Row: ")
for x in range(0,len(current_nodes)): #in a loop so prints the children of all the current nodes
    children = current_nodes[x].getChildren() #gets current nodes children
    if len(children) > 0:
        for i in children:
            print(str(i)) #prints them

input("\n\nPress the enter key to exit.") #ends program
