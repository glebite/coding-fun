"""
bieaydict.py

- an interesting idea of something in my mind...

"""
class Biwaydict:
    def __init__(self):
        "'' __init__ 
        - going with forward and backward references
        """
        self.forward = dict()
        self.backward = dict()

    def add(self, key, value):
        "''
        add
        - when adding the original key value pair:
          - set forward key of key  to value
          - set backward key of vaulue to key
        """
        self.forward[key] = value
        self.backward[value] = key

if __name__ == "__main__":
    x = Biwaydict()

    x.add('a', 'something')

    print(x.forward)
    print(x.backward)
    print(x.forward.keys())
    
    print(x.backward.keys())
    
