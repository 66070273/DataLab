class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if not current_node.left:
                current_node.left = BSTNode(data)
            else:
                self._insert_recursive(current_node.left, data)
        elif data > current_node.data:
            if not current_node.right:
                current_node.right = BSTNode(data)
            else:
                self._insert_recursive(current_node.right, data)

    def traverse(self):
        if not self.root:
            print("This is an empty binary search tree.")
        else:
            print("Preorder: ", end="")
            self.preorder(self.root)
            print("\nInorder: ", end="")
            self.inorder(self.root)
            print("\nPostorder: ", end="")
            self.postorder(self.root)

    def preorder(self, current_node):
        if current_node:
            print(f"-> {current_node.data}", end=" ")
            self.preorder(current_node.left)
            self.preorder(current_node.right)

    def inorder(self, current_node):
        if current_node:
            self.inorder(current_node.left)
            print(f"-> {current_node.data}", end=" ")
            self.inorder(current_node.right)

    def postorder(self, current_node):
        if current_node:
            self.postorder(current_node.left)
            self.postorder(current_node.right)
            print(f"-> {current_node.data}", end=" ")

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

    def delete(self, data):
        if not self.root:
            print(f"Delete Error, {data} is not found in Binary Search Tree.")
            return None
        else:
            deleted, self.root = self._delete_recursive(self.root, data)
            if deleted:
                return data
            else:
                print(f"Delete Error, {data} is not found in Binary Search Tree.")
                return None

    def _delete_recursive(self, current_node, data):
        if not current_node:
            return False, current_node

        if data < current_node.data:
            deleted, current_node.left = self._delete_recursive(current_node.left, data)
        elif data > current_node.data:
            deleted, current_node.right = self._delete_recursive(current_node.right, data)
        else:
            # Case 1: The node has no subtree or one subtree
            if not current_node.left:
                return True, current_node.right
            elif not current_node.right:
                return True, current_node.left
            # Case 2: The node has both subtrees
            current_node.data = self._find_max_recursive(current_node.left)
            deleted, current_node.left = self._delete_recursive(current_node.left, current_node.data)

        return deleted, current_node


def main():
    my_bst = BST()
    while True:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            deleted_data = my_bst.delete(int(data))
            if deleted_data is not None:
                print(f"Deleted: {deleted_data}")
        else:
            print("Invalid Condition")
    my_bst.traverse()

if __name__ == "__main__":
    main()
