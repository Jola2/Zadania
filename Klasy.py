#Zadanie 1

class Cat:
    def __init__(self, name, age, owner, breed):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed
    def cat_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nOwner:{self.owner}\nBreed:{self.breed}")

cat_01 = Cat('Mruczek', 4, 'Peter', 'Perski')
cat_01.cat_info()

cat_01.name = 'Puszek'
cat_01.cat_info()

delattr(cat_01, 'name')
print(getattr(cat_01, 'name', 'Niezdefiniowany')) 

#Zadanie 2

class Cat:
    def __init__(self, name, age, owner, breed):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed
    def cat_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nOwner:{self.owner}\nBreed:{self.breed}")
    def add_age(self):
        self.age += 1

cat_01 = Cat('Mruczek', 4, 'Peter', 'Perski')
cat_01.cat_info()
cat_01.add_age()
cat_01.cat_info()

#Zadanie 3

class Cat:
    def __init__(self, name, age, owner, breed):
        self.name = name
        setattr(self, 'age', age)
        self.owner = owner
        self.breed = breed

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age in range(0, 31):
            self._age = age
        else:
            raise ValueError('The age of the cat must be between 0 and 30')


cat_01 = Cat('Mruczek', 4, 'Peter', 'Perski')

#Zadanie 4

import math

class Wheel:
    def __init__(self, radious):
        setattr(self, 'radious', radious)

    @property
    def radious(self):
        return self._radious

    @radious.setter
    def radious(self, radious):
        if radious > 0:
            self._radious = radious
        else:
            raise ValueError('The radius of the circle must be greater than 0')

    def area(self):
        return 2 * math.pi * self._radious

    def circumference(self):
        return math.pi * self._radious ** 2

    def diameter(self):
        return 2 * self._radious


wheel_01 = Wheel(4)
print(wheel_01.area())
print(wheel_01.circumference())
print(wheel_01.diameter())

#Zadanie 5

class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello! I'm {self.name} {self.last_name} and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, last_name, age, name_of_university, list_of_marks):
        Person.__init__(self, name, last_name, age)
        self.name_of_university = name_of_university
        self.list_of_marks = list_of_marks

    def greeting(self):
        Person.greeting(self)
        print(f"I study on {self.name_of_university} and have marks: {self.list_of_marks}.")

    def new_mark(self, new_mark):
        print("I got a new mark.")
        self.list_of_marks.append(new_mark)



student_01 = Student('Anna', 'Stewart', 21, 'Harvard', [5, 3, 5, 4])
student_01.greeting()
student_01.new_mark(2)
print(student_01.list_of_marks)
