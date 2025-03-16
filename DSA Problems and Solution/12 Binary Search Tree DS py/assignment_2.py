"""
Assignment-21: Binary Search Tree part-2
1.	In class BST, define a method to find minimum value item node.
2.	In class BST, define a method to find maximum value item node.
3.	In class BST, define a method to delete a node from binary search tree.
4.	In class BST, define a method size to return the number of elements present in the BST
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

    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item
    
    def delete(self, data):
        self.root = self.delete_recursive(self.root, data)

    def delete_recursive(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.delete_recursive(root.left, data)
        elif data > root.item:
            root.right = self.delete_recursive(root.right, data)
        else:
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.delete_recursive(root.right, root.item)
        return root
    
    def size(self):
        return len(self.inorder())
    

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

print("Minimum value in BST:", bst.min_value(bst.root))
print("Maximum value in BST:", bst.max_value(bst.root))

print("Size of BST:", bst.size())

bst.delete(50)
print("Inorder Traversal after deleting 50:", bst.inorder())

print("Size of BST after deletion:", bst.size())
