import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, item, x):
        self.item=item
        self.x=x
        self.left=None
        self.right=None
        
class BinaryTree():
    def __init__(self):
        self.root=None
        
    def insert(self, val, x):
        self.root = self._insert(self.root, val, x)
        return self.root is not None

    def _insert(self, node, val, x):
        if node is None:    return Node(val, x)

        if x < node.x:  node.left = self._insert(node.left, val, x)
        else:   node.right = self._insert(node.right, val, x)

        return node

    def preSearch(self, node):
        if node:
            pre.append(node.item)
            if node.left:   self.preSearch(node.left)
            if node.right:  self.preSearch(node.right)
            
    def postSearch(self, node):
        if node:
            if node.left:   self.postSearch(node.left)
            if node.right:  self.postSearch(node.right)
            post.append(node.item)
    
def solution(nodeinfo):
    answer = [[]]
    new_nodeinfo=[]
    
    for i, node in enumerate(nodeinfo):
        new_nodeinfo.append([i+1, node])
    
    new_nodeinfo.sort(key=lambda x : (-x[1][1], x[1][0]))
    tree=BinaryTree()
    
    for node in new_nodeinfo:
        tree.insert(node[0], node[1][0])
    
    global pre, post
    pre=[]
    post=[]
    
    tree.preSearch(tree.root)
    tree.postSearch(tree.root)
    
    answer=[pre, post]
    
    return answer
