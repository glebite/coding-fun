from src.biwaydict import Biwaydict

def test_create():
    x = Biwaydict()
    assert x is not None

def test_add_one():
    x = Biwaydict()
    x.add('name', 'Paul')
    assert x.forward == {'name': 'Paul'}
