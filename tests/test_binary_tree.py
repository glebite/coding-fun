from src.binary_tree import Tree

def test_basic_tree_creation():
    x = Tree()
    assert x is not None

def test_basic_add_one():
    x = Tree()
    x.add_node(5)
    assert x.root.value == 5
