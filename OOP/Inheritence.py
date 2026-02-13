class ParentClass:
    def __init__(self):
        print('calling parent init')

    def parentMethod(self):
        print('calling parent method')

    def setAttr(self, attr):
        self.attr = attr

    def getAttr(self):
        return self.attr

class Childclass(ParentClass):
    def __init__(self):
        print('calling child init')

    def childMethod(self):
        print('calling child method')


c = Childclass()
c.parentMethod()
c.childMethod()
c.setAttr(30)
print('attritbute: ' + str(c.getAttr()))
