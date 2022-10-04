class Animal():
    name=""
    def __init__(self):
        print("Создан питомец")
class Cat(Animal):
    age=0
    colorofcat=""
    def __init__(self):
        Animal.__init__(self)
        print("Родился кот")
    def makeNoise(self):
        print(self.name," говорит Мяу")
myCat=Cat()
myCat.name="Мурка"
myCat.age=1
myCat.colorofcat="белая"
myCat.makeNoise()
