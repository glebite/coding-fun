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

    def delete_node(self, value):
        # find the node, etc..
        # start at the root, find the deepest, rightmost node in the tree
        # as well as the node that we want to delete
        #
        # replace the deepest rightmost node's data with node to be deleted
        #
        # delete the deepest rightmost node
        pass
                
    def display(self):
        """ display """
        if self.root != None:
            self._print(self.root)

    def _print(self, node):
        """ _print """
        if node != None:
            self._print(node.left)
            print(str(node.value)),
            self._print(node.right)

    def to_list(self):
        """ convert to a list """
        if self.root != None:
            path = list()
            return self._to_list(self.root, path)

    def _to_list(self, node, path):
        if node != None:
            self._to_list(node.left, path)
            path.append(node.value)
            self._to_list(node.right, path)
        return path
            
def main():
    """ main """
    x = Tree()
    x.add_node(3)
    x.add_node(5)
    x.add_node(1)
    x.add_node(-1)
    print(x.to_list())
    

if __name__ == "__main__":
    main()
