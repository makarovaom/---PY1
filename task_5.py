import string
from random import sample


def get_random_password(n=8) -> str:
    password = ''
    symbols_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(sample(symbols_, n))
    return password


print(get_random_password())

