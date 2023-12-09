class TestQns2:
    d = 50

    def __init__(self):
        self.a = 5
        self._b = 10
        self.__c = 20

    def method1(self):
        self.method3()
        print(self.a)
        print(self._b)
        print(self.__c)

    @staticmethod
    def method3():
        print("Inside Static")

    @classmethod
    def method4(cls):
        print("inside Class method", cls.d, cls.method3())


class SubClass(TestQns2):

    def method2(self):
        self.method3()
        print(self.a)
        print(self._b)
        print(self.__c)


if __name__ == '__main__':
    obj = SubClass()
    obj.method4()
