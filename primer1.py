from abc import abstractmethod
class Animals:
    def __init__(self, vid, name, age):
        self.vid = vid
        self.name = name
        self.age = age

    @abstractmethod
    def vid_a(self):
        print("Принадлежность: " + self.vid)

    @abstractmethod
    def name_a(self):
        print("Кличка - " + self.name)

    @abstractmethod
    def age_a(self):
        print("Возраст - " + str(self.age))
class Dikie(Animals):
    def __init__(self, vid = "кабан", name = "Гоша", age = 5):
        super().__init__(vid,name,  age)

    def vivod(self):
        print("Это дикое животное")

    def age_a(self):
        print("Возраст дикого животного - " + str(self.age))


class Domashnie(Animals):
    def __init__(self, vid = "кот", name = "Барсик", age = 5):
        super().__init__(vid, name, age)

    def runing(self):
        print("Это домашнее животное")

    def age_a(self):
        print("Возраст домашнего животного - " + str(self.age))
    def age_a(self):
        print("!!!!!!!!- " + str(self.age))
class Morskkie(Animals):
    def __init__(self, vid = "карп", name = "Каспер", age = 1):
        super().__init__(vid, name, age)

    def run(self):
        print("Это морское животное")

    def age_a(self):
        print("Возраст морского животного - " + str(self.age))

cat1 = Animals("собака","Барсик", 3)
cat1.vid_a()
cat1.name_a()
cat1.age_a()
olen = Domashnie("олень","Кузя", 7)
olen.vid_a()
olen.name_a()
olen.age_a()
kaban = Dikie()
kaban.vid_a()
kaban.name_a()
kaban.age_a()