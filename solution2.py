class Node:
    def __init__(self,left,right,val) -> None :
        self.left = left
        self.right = right
        self.val = val


def buildTree(ar,L,R):
    if L == R :
        return Node(None,None,ar[L])
    mid = L + (R - L) // 2

    left = buildTree(ar,L,mid)
    right = buildTree(ar,mid+1,R)
    return Node(left,right,right.val + left.val)


def setArray(ar):
    global root
    global len_ar
    len_ar = len(ar)
    root = buildTree(ar,0,len(ar) - 1)

def rs(root,al,ar,ql,qr):
    # base case
    if al > qr or ar < ql :
        return 0
    # check for overlap of query with current node
    if ql <= al and qr >= ar :
        return root.val
    middle = al + ((ar-al)//2)
    return rs(root.left,al,middle,ql,qr) + rs(root.right,middle+1,ar,ql,qr)

# 5-8
# 2-3
def rangeSum(L,R):
    return rs(root,0,len_ar - 1,L,R)

setArray([4,5,6,7,8,9,11,12,35,66,77])
print(rangeSum(3,5))