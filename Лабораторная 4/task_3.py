def delete(list_, index=None):
    list_new = []
    if index is None:
        list_ = list_[:-1]
        return list_
    else:
        list_.pop(index + 1)
        return list_



print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
