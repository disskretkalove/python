class Animal():
    name = ""
    def __init__(self,newName):
        self.name = newName
    def setName(self, newName):
        self.name = newName
    def getName(self):
        print(self.name)


class Dog(Animal):
    def makeNoise(self):
        print(self.name, " говорит Гав")
    def eat(self):
        print(self.name, " скушала корм")

class Cat(Animal):

    def makeNoise(self):
        print(self.name, " говорит мяу")
    def eat(self):
        print(self.name, " скушал мышку")

class Osa(Animal):
    def makeNoise(self):
        print(self.name, " Делает жалко")
    def eat(self):
        print(self.name, " делает жжжжжжжжжжжжжжжжжжжжжжжж")

newCat = Cat("Пёс")
newCat.setName("Рыжый")
newCat.getName()
newCat.eat()
newCat.makeNoise()

newDog = Dog("Стыд")
newDog.getName()
newDog.eat()
newDog.makeNoise()

smallDog = Dog("Кринж")
smallDog.getName()
smallDog.eat()
smallDog.makeNoise()

osaChad = Osa("Пчела")
osaChad.getName()
osaChad.eat()
osaChad.makeNoise()

