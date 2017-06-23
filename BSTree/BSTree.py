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
                return node
            elif key < node.key:
                return self.insert__( node.left, key, value )
            else:
                return self.insert__( node.right, key, value )
    
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
        return