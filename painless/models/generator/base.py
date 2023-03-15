import secrets
from random import random

from mimesis.locales import Locale
from mimesis import(
    Text,
    
    Numeric,
    Finance,
    Datetime,
    Address,
    Person,
    

)

Locale.EN

class BaseDataGenerator:

    def __init__(self,locale='en'):
        self.person = Person(getattr(Locale,locale.upper()))
        self.finance = Finance(getattr(Locale,locale.upper()))
        self.address = Address(getattr(Locale,locale.upper()))

    def get_random_secret(self,nbytes=20):
        return secrets.token_urlsafe(nbytes)
    
    def get_random_sentences(self,total):
        return self.person.full_name()
    
    def get_random_obj(self,population):
        return random.choice(population)
    

