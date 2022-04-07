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
getattr(cat_01, 'name', 'Niezdefiniowany')

#druga część zadania

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
