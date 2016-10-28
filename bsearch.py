class Node(object):

    def __init__(self, value=0, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def insert(self, value):
        if self.value > value:
            if self.left_child:
                self.left_child.insert(value)
            else:
                self.left_child = Node(value)
        else:
            if self.right_child:
                self.right_child.insert(value)
            else:
                self.right_child = Node(value)

    def view(self):
        if not self.right_child and not self.left_child:
            return str(self.value)

        node_rep  = ''
        if self.left_child:
            node_rep = node_rep + self.left_child.view()

        node_rep = node_rep + str(self.value)

        if self.right_child:
            node_rep = node_rep + self.right_child.view()

        return node_rep
root = Node(5)
root.insert(1)
root.insert(0)
root.insert(3)
root.insert(7)
root.insert(6)
root.insert(10)

print root.view()
