def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if letter in dict_:
                dict_[letter] += 1
            else:
                dict_[letter] = 1
    return dict_

def percent_char(dict_):
    i = 0
    percent_dict = {}
    for char in dict_:
        i += dict_.get(char)
    for char in dict_:
        percent_dict[char] = round((dict_.get(char)/i)*100, 2)
    check = 0
    for char in percent_dict:
        check += percent_dict.get(char)
    return percent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
