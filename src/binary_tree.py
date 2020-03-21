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
        """ __init__ """
        self.root = None

    def get_root(self):
        """  get_root """
        return self.root

    def add_node(self, value):
        """ add_node """
        if self.root == None:
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        """ _add_node """
        if value < node.value:
            if node.left != None:
                self._add_node(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right != None:
                self._add_node(value, node.right)
            else:
                node.right = Node(value)
                
    def display(self):
        """ display """
        if self.root != None:
            self._print(self.root)

    def _print(self, node):
        """ _print """
        nodes = list()
        if node != None:
            self._print(node.left)
            print(str(node.value))
            nodes.append(str(node.value))
            self._print(node.right)
        return
            
def main():
    """ main """
    x = Tree()
    x.add_node(3)
    x.add_node(5)
    x.add_node(1)
    print(x.display())
    

if __name__ == "__main__":
    main()
