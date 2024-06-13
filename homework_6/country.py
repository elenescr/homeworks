from abc import ABC, abstractmethod

class Country (ABC):

    @abstractmethod
    def greeting(self):
        pass
    @abstractmethod
    def  passport_control (self):
        pass
    @abstractmethod
    def warning(self):
        pass


class Georgia(Country):
    def __init__(self):
        self.__area = 69700
        self._goverment = "Unitary parliamentary republic"
        self.motto="Strength is in Unity"

    def greeting(self):
        print (f"Hello, wellcome to our country !")

    def passport_control(self):
        print ("show us passport and visa!")

    def warning(self):
        print ("Please read carefully list of itmes you can't bring across thr boarder!")

sakartvelo = Georgia()
print (sakartvelo.motto)
print(sakartvelo._goverment)
sakartvelo.warning()
sakartvelo.greeting()
