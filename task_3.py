from random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) != 15:
        random_int = randint(-10, 10)
        if random_int not in list_:
            list_.append(random_int)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
