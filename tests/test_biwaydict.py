from src.biwaydict import Biwaydict

def test_create():
    x = Biwaydict()
    assert x is not None

def test_add_one():
    x = Biwaydict()
    x.add('name', 'Paul')
    assert x.forward == {'name': 'Paul'}

def test_add_two():
    x = Biwaydict()
    x.add('a', 'value_a')
    x.add('b', 'value_b')
    assert x.forward == {'a': 'value_a', 'b':'value_b'} 
    assert x.backward == {'value_a': 'a', 'value_b': 'b'}
