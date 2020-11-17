class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.data == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print tree
    def Print_Tree(self):
        if self.left:
            self.left.Print_Tree()
        print(self)
        if self.right:
            self.right.Print_Tree()
root = Node(10)
root.insert(7)
root.insert(30)
root.insert(6)
root.Print_Tree()