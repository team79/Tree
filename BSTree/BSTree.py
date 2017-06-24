class BSTreeNode(object):
    def __init__( self, left = None, right = None, key = 0, value = 0 ):
        self.left = left
        self.right = right
        self.value = value
        self.key = key
        
class BSTree(object):
    def __init__( self ):
        self.root = None
        
    def __setitem__ ( self, key, value ):
        self.root = self.insert__( self.root, key, value )
    
    def insert__( self, node, key, value ):
        if node == None:
            return BSTreeNode( None, None, key, value )
        else:
            if node.key == key:
                node.value = value
            elif key < node.key:
                node.left = self.insert__( node.left, key, value )
            else:
                node.right = self.insert__( node.right, key, value )
        return node
    
    def __getitem__ ( self, key ):
        root = self.root
        while root != None:
            if key == root.key:
                return root.value
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return None
    
    def delete( self, key ):
        self.root = self.delete__( self.root, key )
        
    def delete__( self, node, key ):
        if key == node.key:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                temp = self.findMin( node.right )
                node.key = temp.key
                node.value = temp.value
                node.right = self.delete__( node.right, temp.key )
        elif key < node.key:
            node.left = self.delete__( node.left, key )
        else:
            node.right = self.delete__( node.right, key )
        return node
                
        
        
    def findMin( self, node ):
        if node.left != None:
            return self.findMin( node.left )
        else:
            return node
            
def Traversal( root, deep ):
    if root.right != None:
        Traversal( root.right, deep + 1 )
    for i in range(deep):
        print("\t", end = " ")
    print(root.key)
    if root.left != None:
        Traversal( root.left, deep + 1 )

X = BSTree()
X[1] = 1
X[2] = 2
X[0] = 0
X[3] = 3
X[1.5] = 1.5
X[1.55] = 1.55
Traversal( X.root, 0 )
print("")
print("")
print("")
print("")
X.delete( 2 )
Traversal( X.root, 0 )