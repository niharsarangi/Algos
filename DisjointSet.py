class Node:
    def __init__(self,data,rank=0):
        self.data=data
        self.parent=self
        self.rank=rank
        
def find(x):
    if x != x.parent:
        x.parent=find(x.parent)
    return x.parent

def merge(x,y):
    px=find(x)
    py=find(y)
    if px.rank > py.rank:
        py.parent=px
    else:
        px.parent=py
        
    if px.rank==py.rank:
        py.rank+=1

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)

merge(a,b)
merge(d,c)
merge(b,c)
