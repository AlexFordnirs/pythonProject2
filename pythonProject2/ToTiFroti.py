class Person:
    def __init__(self, name, KG):
        self.__name = name
        self.__KG = KG



    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__KG

    def __sub__(self, name, other):
        if isinstance(other,Person):
            if(self.__name not in name):
                return Person(self.__name,self.__KG-self.__KG)
        else: return None

    def __add__(self,name, other):
        if isinstance(other, Person):
            if (self.__name not in name):
                return Person(self.__name, self.__KG + self.__KG)
        else:
            return None


    def __lt__(self, other):
        print('moon light')
        return self.__KG < other

    def __le__(self, other):
        print('moon light')
        return self.__KG <= other

    def __eq__(self, other):
        print('moon light')
        return self.__KG == other

    def __ne__(self, other):
        print('moon light')
        return self.__KG != other

    def __gt__(self, other):
        print('moon light')
        return self.__KG > other

    def __ge__(self, other):
        print('moon light')
        return self.__KG >= other


D=Person("Tom",100)
print(D<20)
print(D<=20)
print(D==20)
print(D!=20)
print(D>20)
print(D>= 20)
