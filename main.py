from Authorization.Authorization import Authorization
from Registration.Registration import Registration
from Student.Student import Student
from Teacher.Teacher import Teacher

def my_Authorization():
    my_Authorization = Authorization()
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    password = password.replace('a', '1').replace('c', '2')
    data = my_Authorization.getUsers(login, password)
    if data != ():
        user = data[0]
        if user['status'] == "Student":
            print('Добро пожаловать в личный кабинет, ' + user['name'],user['surname'])
            my_Student = Student()
            my_Student.menu_student()
        elif user['status'] == 'Teacher':
            print('Добро пожаловать в личный кабинет, ' + user['name'], user['surname'])
            my_Teacher = Teacher()
            my_Teacher.menu_teacher()
    else:
        print('Incorrect login or password!')
        Start()


def my_Registration():
    my_Registration = Registration()
    my_Registration.addUser(input('Введите имя: '),input('Введите фамилию: '),input('Введите логин: '),
                            input('Введите пароль: '),
                            input('Введите статус. Student или Teacher: '))


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
            print('Выберите пункт меню')

Start()
