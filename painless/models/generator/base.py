import secrets
import random
import logging
from typing import List,Any
from mimesis.locales import Locale
from mimesis import(
    Text,
    Numeric,
    Finance,
    Datetime,
    Address,
    Person,
    
    
    

)
coreLogger = logging.getLogger('core')
Locale.EN

class BaseDataGenerator:
    """ that is used for generating random data based on
    the specified locale. It uses the mimesis library to 
    generate data for various purposes such as generating
    random words, random objects from a given population,
    and random names, addresses, and finance information 
    for a given locale."""

    def __init__(self,locale='en'):
        self.person = Person(getattr(Locale,locale.upper()))
        self.finance = Finance(getattr(Locale,locale.upper()))
        self.address = Address(getattr(Locale,locale.upper()))
        self.text = Text(getattr(Locale,locale.upper()))

    def get_random_secret(self,nbytes=20):
        """

        Parameters
        ----------
        nbytes : number of digits 
            (Default value = 20)

        Returns
        -------

        """
        return secrets.token_urlsafe(nbytes)
    
    def get_random_person(self):
        """ Returns a random full name of a person."""
        return self.person.full_name()
    
    def get_random_obj(self,population):
        """

        Parameters
        ----------
        population :
            

        Returns
        -------

        """
        return random.choice(population)
    
    def get_random_words(self,total):
        """
        Returns a list of random words of the specified quantity.
        Parameters
        ----------
        total :
            the quantity

        Returns
        -------

        """
        return self.text.words(quantity=total)
    
    def get_random_pic_name(self,format='jpg'):
        """
        Returns a random name for a picture file with the specified format.
        Parameters
        ----------
        format :
            (Default value = 'jpg')

        Returns
        -------

        """
        return f'generated-pic-{self.get_random_secret(5)}.{format}'

    def add_to_m2m(
            self,
            objs:List[Any],
            target_field:str,
            item_per_obj:int,
            item):
        """Add a number of randomly selected objects from a list to many to many field
        this method select 'item pre obj' number of objects randomly from the 'objs'
        list and add them to the ManyToManyField on the model instance . the 'objs'
        List must not be empty , or an indexerror will raised.
        
        objs: A list of objects to select from
        target field : the name of the ManyToMany on the model instance .
        item_pre_obj: the number of objects to add to the ManyToMany Field.
        item : the type of the model that the ManyToMany field belongs to .

    

        """

        
        attr = getattr(item,target_field)
        try:
            item_to_add = list(map(lambda _: random.choice(objs), range(item_per_obj)))
        except IndexError as e :
            
            coreLogger.debug(
                "`objs` are empty. please ensure population in not non",
                exc_info=True
                )
            raise IndexError(
                "`objs` are empty. please ensure population in not non"
                )
            
        attr.add(*item_to_add)