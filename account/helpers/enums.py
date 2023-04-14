from enum import StrEnum


class RegexPatternEnum(StrEnum):
    IRAN_PHONE_NUMBER = r"^(\+98|0?9\d{9}$)"
    INTERNATIONAL_PHONE_NUMBER = r'^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
    USERNAME = r'^[a-zA-Z][a-zA-Z0-9.]{2,14}$'
    NAME = r'^[a-zA-Z][a-zA-Z\s]{2,14}$'