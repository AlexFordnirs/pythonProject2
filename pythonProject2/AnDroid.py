class Droid:
    def __init__(self, name="Droid"):
        self.__name = name

    @property
    def name(self):
        return self.__name

class R2D2(Droid):
    def __init__(self, name="R2D2"):
        self.__name = name

    @property
    def name(self):
        return self.__name

class CERO(Droid):
    def __init__(self, name="CERO"):
        self.__name = name

    @property
    def name(self):

       return self.__name

class BB8(R2D2):
    def __init__(self, name="BB8"):
        self.__name = name

    @property
    def name(self):
        return self.__name



c= CERO("Grik")
print(c.name)

