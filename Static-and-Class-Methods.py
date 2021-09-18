# Static and Class Methods
class Person():
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1 # class variables

    @classmethod
    def getPopulation(cls):
        return cls.population

    @classmethod
    def newBorn(cls, name):
        return cls(name, 0)

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')


personOne = Person('T', 18)
newPerson = Person.newBorn('B')

print('Population', Person.getPopulation())

print('Is 22 Adult?', Person.isAdult(22))

personOne.display()
newPerson.display()