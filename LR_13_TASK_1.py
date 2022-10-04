class Cat():
    name = ""
    color = ""
    weight = 0

    def meow(self):
        print(self.name, "мяукнул")


myCat = Cat()
myCat.name = "мурка"
myCat.color = "белая"
myCat.weight = 4
myCat.meow()
