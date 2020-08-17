class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 320
    def method(self):
        return 'instance method called', self, self.x + self.y

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

C = MyClass()

print(MyClass().method())
print(MyClass.classmethod())
print()
