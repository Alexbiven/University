

from Authorization.Authorization import Authorization
from Registration.Registration import Registration

def my_Authorization():
    my_Authorization = Authorization('qwerty', 'sdf234')
    print('Логин: ' + my_Authorization.login, 'Пароль: ' + my_Authorization.password)

def my_Registration():
    my_Registration = Registration('qwertyке', 'sdf23154')
    print('Логин: ' + my_Registration.login, 'Пароль: ' + my_Registration.password)

def Start():
    while True:
        type = int(input('МЕНЮ ВЫБОРА:' '\n' '1. Авторизация' '\n' '2. Регистрация' '\n' '3. Выход' '\n' 
                         'Выберите пункт: '))
        if type == 1:
            my_Authorization()
        elif type == 2:
            my_Registration()
        elif type == 3:
            Start()
Start()