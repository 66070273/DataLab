class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_left(self):
        return self.left

    def set_left(self, new_left):
        self.left = new_left

    def get_right(self):
        return self.right

    def set_right(self, new_right):
        self.right = new_right

data_input = int(input())
node = BSTNode(data_input)
print(node.get_data())
print(node.get_left())
print(node.get_right())
