"""
Assignment-20: Binary Search Tree part-I
1.	Define a class Node with instance variables left, item and right. The variables left and right are used to refer left and right child node. The item variable is used to hold data item.
2.	Define a class BST to implement Binary Search Tree data structure. Make __init__() method to create root instance variable to hold the reference of root node.
3.	In class BST, define insert method to store new data item in the binary search tree.
4.	In class BST, define a search method to find a given item in the binary search tree and returns the node reference. It returns None if search failed.
5.	In class BST, define a method to implement inorder traversal.
6.	In class BST, define a method to implement preorder traversal.
7.	In class BST, define a method to implement postorder traversal.
"""

class Node:
    def __init__(self, item = None, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right 

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_recursive(self.root, data)

    def insert_recursive(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.item:
            root.left = self.insert_recursive(root.left, data)
        elif data > root.item:
            root.right = self.insert_recursive(root.right, data)
        return root
    
    def search(self, data):
        return self.search_recursive(self.root, data)
    
    def search_recursive(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.search_recursive(root.left, data)
        if data > root.item:
            return self.search_recursive(root.right, data)
        
    def inorder(self):
        store = []
        self.inorder_recursive(self.root, store)
        return store
    
    def inorder_recursive(self, root, store):
        if root is not None:
            self.inorder_recursive(root.left, store)
            store.append(root.item)
            self.inorder_recursive(root.right, store)

    def preorder(self):
        store = []
        self.preorder_recursive(self.root, store)
        return store
    
    def preorder_recursive(self, root, store):
        if root is not None:
            store.append(root.item)
            self.preorder_recursive(root.left, store)
            self.preorder_recursive(root.right, store)
    
    def postorder(self):
        store = []
        self.postorder_recursive(self.root, store)
        return store
    
    def postorder_recursive(self, root, store):
        if root is not None:
            self.postorder_recursive(root.left, store)
            self.postorder_recursive(root.right, store)
            store.append(root.item)

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:", bst.inorder())  
print("Preorder Traversal:", bst.preorder())  
print("Postorder Traversal:", bst.postorder())  

search_result = bst.search(60)
print("Search 60:", "Found" if search_result else "Not Found")

search_result = bst.search(100)
print("Search 100:", "Found" if search_result else "Not Found")