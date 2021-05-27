#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def Word_Modify(v_word):
    v_word = v_word.capitalize()
    return v_word


def Print_Long_String(ls):
    v_string_list = ls.split(' ')
    res = ''
    for i in v_string_list:
        res += ' ' + Word_Modify(i)
    return res


tmp_str = input('Введите предложение')
print(str(Print_Long_String(tmp_str)))