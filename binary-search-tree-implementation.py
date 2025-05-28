class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    # Search
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # In-order Traversal (Left, Root, Right)
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.key, end=' ')
            self._inorder(root.right)

    # Pre-order Traversal (Root, Left, Right)
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root:
            print(root.key, end=' ')
            self._preorder(root.left)
            self._preorder(root.right)

    # Post-order Traversal (Left, Right, Root)
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.key, end=' ')

    # Find minimum node
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Deletion
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root


tree = BST()
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    tree.insert(v)

print("Inorder Traversal:")
tree.inorder()

print("Search 60:", tree.search(60) is not None)

print("Deleting 20...")
tree.delete(20)
tree.inorder()

print("Deleting 30...")
tree.delete(30)
tree.inorder()

print("Deleting 50 (root)...")
tree.delete(50)
tree.inorder()

print("Preorder Traversal:")
tree.preorder()

print("Postorder Traversal:")
tree.postorder()
