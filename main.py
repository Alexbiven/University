
from Authorization.Authorization import Authorization
from Registration.Registration import Registration
from Teacher.Teacher import Teacher
from Student.Student import Student

def my_Authorization():
    my_Authorization = Authorization('qwerty', 'sdf234')
    print('Логин: ' + my_Authorization.login, 'Пароль: ' + my_Authorization.password)

def my_Registration():
    my_Registration = Registration()
    my_Registration.addUser(input('Введите имя: '),input('Введите фамилию: '),input('Введите логин: '),
                            input('Введите пароль: '), input('Введите статус: '))

def Edition_info():
    my_Teacher = Teacher()
    my_Teacher.edit_information(int(input('Введите номер курса: ')), input('Введите название факультета: '),
                                int(input('Введите оценку: ')), float(input('Введите средний бал: ')))

def Searching_info():
    my_Student = Student()
    my_Student.search_information()


def Start():
    while True:
        type = int(input('МЕНЮ ВЫБОРА:' '\n' '1. Авторизация' '\n' '2. Регистрация' '\n'  
                         'Выберите пункт: '))
        if type == 1:
            my_Authorization()
            break
        elif type == 2:
            my_Registration()
            break
        else:
            print('Error')


def Human_menu():
    while True:
        act = int(input('МЕНЮ ВЫБОРА:' '\n' '1. Преподаватель  ' '\n' '2. Студент '  '\n'
                         'Выберите пункт: '))
        if act == 1:
            Edition_info()
            break
        elif act == 2:
            Searching_info()
            break
        else:
            print('Error')



def main():
    Start()
    Human_menu()

main()