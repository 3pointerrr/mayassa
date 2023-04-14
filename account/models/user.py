from django.contrib.auth.models import AbstractUser
from django.db import models
from painless.mixin_files import TimeStampMixin
from django.contrib.auth.models import (
        UnicodeUsernameValidator,
        AbstractUser  
    )
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MaxLengthValidator,
    RegexValidator,
    MinLengthValidator,
    
)
from account.helpers.enums import RegexPatternEnum
class User(AbstractUser,TimeStampMixin):
    """
    Custom mode user class , overriding `username` and change
    USERNAME_FIELD to phone number
    """

    username = None
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=15,
        unique=True,
        help_text=_(
            "Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[
        username_validator,
        RegexValidator(RegexPatternEnum.USERNAME),
        MaxLengthValidator(15),
        MinLengthValidator(3)
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
            "max_length": _("User name must be at max 15 character"),
            "min_length": _("user name must be at least 3 character"),
            "invalid": _(
        "User name must start with character , then it "
        "could have numbers and character and `.` ."
        ),

            

        },
    )
    first_name = models.CharField(
        _("first name")
        , max_length=150, 
        blank=True,
        null=True,
        validators=[
        RegexValidator(RegexPatternEnum.USERNAME),
        MaxLengthValidator(15),
        MinLengthValidator(3)
        ],
        
    )
    last_name = models.CharField( 
        _("last name"),
        max_length=150, 
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        _("Phone Number"),
        max_length=15,
        validators=[
        RegexValidator(RegexPatternEnum.IRAN_PHONE_NUMBER),
        MaxLengthValidator(15),
        MinLengthValidator(10)
                    ],
        unique=True,
        # TODO
        help_text=_("to do !")
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
        null=True)
    USERNAME_FIELD = 'phone number'