import secrets
import random

from mimesis.locales import Locale
from mimesis import (
    Finance,
    Person,
    Text,
    Numeric,
    Datetime,
    Address,
    Food,
    
)

# from essential_generators import DocumentGenerator


#create base data genarator
class BaseDataGenerator():

    def __init__(self, locale='en'):
        self.numeric = Numeric()
        self.text = Text(getattr(Locale, locale.upper()))

    def get_random_secret(self, nbytes=10):
        #generate random string
        return secrets.token_urlsafe(nbytes)
    
    def get_random_sentences(self, total):
        return self.text.text(quantity=total)
    
    def get_random_word(self, total):
        return self.text.words(quantity= total)
        
    def get_random_obj(self, population):
        return random.choice(population)
    
    def get_random_numeric(self):
        return self.numeric.integers(start=20,end=60,n=1)[0]
    
    
    
