#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def f_show_personal_data(First_Name, Last_Name, BD, email, phone):
    """" Приобразуем данные по пользователю в строку"""
    res = First_Name + ' ' + Last_Name+ ' год прождения ' + BD + ' E-Mail ' + email + ' Тел ' + phone
    return res


var_FN = input('Введите имя ')
var_LN = input('Введите фамилию ')
var_BD = input('Введите год рождения')
var_phone = input('Введите телефон')
var_email = input('Введите email')

print(f_show_personal_data (First_Name=var_FN, BD=var_BD, email=var_email, Last_Name=var_LN, phone=var_phone ))