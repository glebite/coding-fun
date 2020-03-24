from src.binary_tree import Tree

def test_basic_tree_creation():
    x = Tree()
    assert x is not None

def test_basic_add_one():
    x = Tree()
    x.add_node(5)
    assert x.root.value == 5

def test_basic_add_two_to_list():
    x = Tree()
    x.add_node(1)
    x.add_node(3)
    assert x.to_list() == [1,3]

