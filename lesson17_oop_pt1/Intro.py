class Human:
    hands = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_jump(self):
        print(self.name, "прыгнул")


human_1 = Human("Richard", 18)
human_2 = Human("Kate", 74)

human_1.do_jump()
human_2.do_jump()
