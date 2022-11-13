def get_random_password() -> str:
    import string
    from random import sample
    password = ''
    length_ = 8
    symbols_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(sample(symbols_, length_ ))
    return password


print(get_random_password())