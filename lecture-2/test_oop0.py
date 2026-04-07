class Dog:
    def __init__(yo, iname, icolor, iage):
        yo.name = iname
        yo.color = icolor
        yo.age = iage

    def bark(yo):
        return f"Woof! I'm {yo.name}!"


dog1 = Dog("Buddy", "Brown", 5)
dog2 = Dog("Guardián", "Black", 3)
dog3 = Dog("Killer", "Gray", 7  )
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())