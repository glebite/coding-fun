"""
bieaydict.py

- an interesting idea of something in my mind...

"""
class Biwaydict(dict):
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        if key in self:
            del self[self[key]]
        if value in self:
            del self[value]
        super().__setitem__(key, value)
        super().__setitem__(value, key)


if __name__ == "__main__":
    x = Biwaydict()

    x['what'] = "something"
    print(x)
