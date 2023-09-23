from typing import Final

class Tree:
    pass

class Leaf(Tree):
    def __init__(self,val)-> None:
        super().__init__()
        self.val:Final=val

class Branch(Tree):
    def __init__(self,val,left:Tree,right:Tree) -> None:
        super().__init__()
        self.val = val
        self.left:Final[Tree]=left
        self.right:Final[Tree] = right


def treeSize(t:Tree)-> int:
    if t is None: return 0
    elif isinstance(t,Leaf): return 1
    else: return 1 + treeSize(t.left) + treeSize(t.right)

def maxVal(t:Tree,mx):
    if isinstance(t,Leaf): 
        return t.val
    else:
        return mx(t.val, mx(maxVal(t.left, mx), maxVal(t.right, mx)))   

    
def maxDepth(t:Tree) -> int:
    if isinstance(t,Leaf): return 0
    else: return 1 + max(maxDepth(t.left), maxDepth(t.right))

def mapTree(t:Tree,mp):
    if isinstance(t,Leaf):
        return Leaf(mp(t.val))
    else:
        return Branch(mp(t.val),mapTree(t.left,mp),mapTree(t.right,mp))
    
def fold(t:Tree,bs,acc):
    if isinstance(t,Leaf):
        return bs(t.val)
    else:
        return acc(bs(t.val),acc(fold(t.left,bs,acc),fold(t.right,bs,acc)))


t = Branch(40,Branch(20,Leaf(10),Leaf(30)), Branch(60,Leaf(5),Leaf(70)))