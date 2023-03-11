from mimesis import Numeric

class BaseDataGenerator():

    def __init__(self, locale='en'):
        self.numeric = Numeric()

    def get_random_numeric(self):
        return self.numeric.integers(start=20,end=60,n=1)[0]

f= BaseDataGenerator()
print(f.get_random_numeric())