import datetime as DT
import time as TM
# Меню выбора задания урока
print('Выберите номер задания:')
print('Задание 1: Запросить ФИО , дату рождения, высичлить возраст')
print('Задание 2: Перевод секунд в часы, минуты, секунды')
print('Задание 3: сумму чисел n + nn + nnn')
print('Задание 4: Максимальная цифра в веденном числе')
print('Задание 5: Прибыльность и рентабельность фирмы')
print('Задание 6: Спортсмен и бег')

v_Part = int(input('Укажите номер задания'))

if v_Part == 1:
    p_Name = input('Введите Имя :')
    p_First_Name = input('Введите Фамилию :')
    p_Second_Name = input('Введите Отчетсво :')
    print('Здраствуйте ' +  p_First_Name + ' ' + p_Name + ' ' + p_Second_Name)
    p_bd_string = input('Введите дату рождения в формате ДД.ММ.ГГГГ')
    p_bd = DT.datetime.strptime(p_bd_string, '%d.%m.%Y').date()
    p_today = DT.datetime.today()
    print('Ваш возраст - ' + str(p_today.year-p_bd.year) + ' лет')
elif v_Part == 2:
    p_Sec_Total = int(input('Введите количество секунд :'))
    p_Hour = int(p_Sec_Total / 3600)
    p_Min = int((p_Sec_Total - p_Hour * 3600) / 60)
    p_Sec = (p_Sec_Total - p_Hour * 3600  - p_Min * 60)
    print('Это значение эквивалентно = Часов ' + str(p_Hour) + ' Мин ' + str(p_Min) + ' Сек ' + str(p_Sec))
    print('Или альтернативно преобразовано ' + str(TM.strftime("%H:%M:%S", TM.gmtime(p_Sec_Total) )))
elif v_Part == 3:
    p_N = (input('Введите число N :'))
    p_NN = p_N+p_N
    p_NNN = p_N+p_N+p_N
    p_Sum = int(p_N) + int(p_NN) + int(p_NNN)
    print('Сумма N+NN+NNN =' + str(p_Sum))
elif v_Part == 4:
    p_Z = (input('Введите число Z в котором определим наибольшую цифру :'))
    p_Z = list(p_Z)
    i = 0
    max_value = p_Z[0]
    while i < len(p_Z):
        if max_value < p_Z[i]:
            max_value = p_Z[i]
        i = i + 1
    print('Самая большая цифра ' + str(max_value) + ' в числе ' + "".join(p_Z))
elif v_Part == 5:
    p_Revenue = float(input('Введите выручку фирмы :'))
    p_Cost = float(input('Введите  издержки фирмы :'))
    p_Income = p_Revenue - p_Cost
    if (p_Income)>0:
        print('У вас есть прибль =' + str(p_Income))
        print('Ваша рентабельность = ' + str(round(p_Revenue/p_Income, 3)) )
        p_Empl = int(input('Введите  количество сотрудников фирмы :'))
        print('Каждый сотрудник заработал Вам = ' + str(round(p_Income/p_Empl, 2)))
    else:
        print('Вы работаете с убытком')
elif v_Part == 6:
    p_Distance = float(input('Введите сколько КМ бегает спортсмен на тренировке :'))
    p_Target_Distance = float(input('Введите цель - сколько КМ он должен пробежать :'))
    p_DayCount = 1
    p_Progress = p_Distance
    while p_Progress <= p_Target_Distance:
        p_Progress = p_Progress+p_Progress * 0.1
        p_DayCount = p_DayCount + 1
        print(' День ' + str (p_DayCount) + ' дистанция ' + str(round(p_Progress,2)) + ' км')
    print('Потребуется ' + str (p_DayCount) + ' дней тренировок')