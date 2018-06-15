class Duck(object):

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack Quack")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)