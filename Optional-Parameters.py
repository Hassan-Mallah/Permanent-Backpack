def func(x=1):
    return x **2


def func2(word, add=5, freq=1):
    print(word*(add + freq))


# class example
class Car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, show_all=False):
        if show_all:
            print('This car is a {} {} from {}, it is {} and has {} kms'.format(self.make, self.model, self.year,
                                                                                self.condition, self.kms))
        else:
            print('This car is a {} {} from {}.'.format(self.make, self.model, self.year))


whip = Car('Ford', 'Fusion', 2012)
whip.display(True)
