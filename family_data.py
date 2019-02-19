class Kid:
    def __init__(self, name="",  age=-1):
        self.name = name
        self.age = age


class Family:
    def __init__(self):
        self.parents = []
        self.kids = []

    def add_kid(self, kid):
        self.kids.append(kid)


