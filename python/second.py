class Pavan:
    def __init__(self, name):
        self.name = name


class Veena(Pavan):
    pass


user1 = Pavan("Veena")
print(user1.name)

user2 = Veena("Arnav")
print(user2.name)
