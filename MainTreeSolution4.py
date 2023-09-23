from solution4 import *

t = Branch(40,Branch(20,Leaf(10),Leaf(30)), Branch(60,Leaf(5),Leaf(70)))

if treeSize(t)!=7:
    print('wrong answer to tree size (-10)')

if maxVal(t,lambda x,y: x if x>y else y)!= 70:
    print('wrong answer to max val (-10)')

if maxDepth(t)!=2:
    print('wrong answer to tree max depth (-10)')

if maxVal(mapTree(t, lambda x: x/10), lambda x,y: x if x>y else y) !=7 :
    print('wrong ans for maxVal (-25)')
    
if fold(t,lambda x:1, lambda x,y:x+y) != 7:
    print('wrong answer to tree size with fold (-25)')

        
if fold(t,lambda x: x, lambda x,y:max(x,y)) != 70:
    print('wrong answer to max val with fold (-25)')

print("done")