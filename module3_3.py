    #1.Функция с параметрами по умолчанию:

#def print_params(a = 1, b = 'строка', c = True):
#    print(a, b, c)

#print_params() - работает верно, вывод в консоль: 1 строка True
#print_params(b = 25) - работает вработает верно, вывод на консоль: 1 25 True
#print_params(c = [1,2,3]) - работает верно, вывод на консоль: 1 строка [1, 2, 3]


    #2.Распаковка параметров:

#def print_params(a, b, c):
#    print(a, b, c)

#values_list = [32, 'Hello', True]
#values_dict = {'a':15, 'b':'Bye', 'c':False}

#print_params(*values_list) - работает верно, вывод в консоль: 32 Hello True
#print_params(**values_dict) - работает верно, вывод в консоль: 15 Bye False


    #3.Распаковка + отдельные параметры:

def print_params(a, b, c):
    print(a, b, c)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42) # работает верно, для проверки 1 и 2 заданий их нужно по отдельности раскомментировать