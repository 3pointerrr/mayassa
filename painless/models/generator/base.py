import secrets
import random

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

        self.text = Text(getattr(Locale,locale.upper()))

    def get_random_secret(self,nbytes=20):
        return secrets.token_urlsafe(nbytes)
    
    def get_random_person(self):
        return self.person.full_name()
    
    def get_random_obj(self,population):
        return random.choice(population)
    
    def get_random_words(self,total):
        return self.text.words(quantity=total)
    
    def get_random_pic_name(self,format='jpg'):
        return f'generated-pic-{self.get_random_secret(5)}.{format}'
