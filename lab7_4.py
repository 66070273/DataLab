class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left:
                self._insert_recursive(current_node.left, data)
            else:
                current_node.left = BSTNode(data)
        elif data > current_node.data:
            if current_node.right:
                self._insert_recursive(current_node.right, data)
            else:
                current_node.right = BSTNode(data)

    def preorder(self):
        if not self.root:
            return
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, current_node):
        if current_node:
            print(f"-> {current_node.data}", end=" ")
            self._preorder_recursive(current_node.left)
            self._preorder_recursive(current_node.right)

    def inorder(self):
        if not self.root:
            return
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node:
            self._inorder_recursive(current_node.left)
            print(f"-> {current_node.data}", end=" ")
            self._inorder_recursive(current_node.right)

    def postorder(self):
        if not self.root:
            return
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, current_node):
        if current_node:
            self._postorder_recursive(current_node.left)
            self._postorder_recursive(current_node.right)
            print(f"-> {current_node.data}", end=" ")

    def traverse(self):
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('\nInorder: ', end='')
        self.inorder()
        print('\nPostorder: ', end='')
        self.postorder()
        print()

    def find_min(self):
        if not self.root:
            return None
        return self._find_min_recursive(self.root)

    def _find_min_recursive(self, current_node):
        if current_node.left:
            return self._find_min_recursive(current_node.left)
        return current_node.data

    def find_max(self):
        if not self.root:
            return None
        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, current_node):
        if current_node.right:
            return self._find_max_recursive(current_node.right)
        return current_node.data

def main():
    """Data Structures and Algorithms Lab – Binary Search Tree"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
