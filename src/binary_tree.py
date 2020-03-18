"""
binary_tree
"""

class Node:
    """ Node """
    def __init__(self, value=None):
        """ __init__ """
        self.value = value
        self.left = None
        self.right = None

class Tree:
    """ Tree """
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add_node(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        if val < node.value:
            if node.left = None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right != None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    
def main():
    pass

if __name__ == "__main__":
    main()
