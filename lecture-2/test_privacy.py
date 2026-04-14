class Person:
    def __init__(self,idi,name):
        self.id=idi
        self.__name=name
    
    def sayHi(self):
        print(f'Hi I\'m {self.__name}')


person0=Person(55555,"Adolfo")
person0.sayHi()
print(person0.id)
print(person0.__name)