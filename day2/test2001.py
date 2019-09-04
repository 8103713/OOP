class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "my name is %s,my weight is %.2f" % (self.name, self.weight)

    def run(self):
        self.weight -= 1
        print("runrunrun  %.2f" % self.weight)

    def eat(self):
        self.weight += 1
        print("eateateat  %.2f" % self.weight)


xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()

# 打印对象的时候会自动运行str方法
print(xiaoming)
