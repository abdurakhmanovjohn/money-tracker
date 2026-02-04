import re
from django.core.exceptions import ValidationError

UZ_PHONE_REGEX = re.compile(
  r"^(?:\+998)?[ -]?\d{2}[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}$"
)

def phone_number_validator(value):
    if not UZ_PHONE_REGEX.match(value):
        raise ValidationError("Enter a valid Uzbekistan phone number!")
