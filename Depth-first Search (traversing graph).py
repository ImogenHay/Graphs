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
b.addChild(a)
c.addChild(f)
c.addChild(d)
c.addChild(a)
d.addChild(g)
d.addChild(h)
d.addChild(e)
d.addChild(c)
e.addChild(d)
f.addChild(j)
f.addChild(g)
f.addChild(c)
g.addChild(f)
g.addChild(d)
h.addChild(d)
j.addChild(h)
j.addChild(f)
k.addChild(b)

done = []
node = a
print(node)
done.append(node)

x = 1
while x > 0:
    if (node.getChildren())[0] in done:
        node
        x = 0
    else:
        node = (node.getChildren())[0]
        done.append(node)
        print(node)



done.remove(done[-2])
x = 1
i = 0

while x > 0:
    while (node.getChildren())[int(i)] in done:
        i = i + 1

    node = (node.getChildren())[int(i)]
    done.append(node)
    print(node)
    x = 0



        




input("\n\nPress the enter key to exit.")
