
from Authorization.Authorization import Authorization
from Registration.Registration import Registration

def my_Authorization():
    my_Authorization = Authorization('qwerty', 'sdf234')
    print('Логин: ' + my_Authorization.login, 'Пароль: ' + my_Authorization.password)

def my_Registration():
    my_Registration = Registration()
    my_Registration.addUser(input('Введите имя: '),input('Введите фамилию: '),input('Введите логин: '),
                            input('Введите пароль: '), input('Введите статус: '))


def Start():
    while True:
        type = int(input('МЕНЮ ВЫБОРА:' '\n' '1. Авторизация' '\n' '2. Регистрация' '\n' '3. Выход' '\n' 
                         'Выберите пункт: '))
        if type == 1:
            my_Authorization()
            break
        elif type == 2:
            my_Registration()
            break
        else:
            print('Error')
Start()