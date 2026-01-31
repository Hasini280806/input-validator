import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_valid_age(age):
    return age.isdigit() and 0 < int(age) <= 120
