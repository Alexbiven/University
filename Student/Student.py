from DataBase import DataBase


class Student:
    def __init__(self, login):
        self.login = login

    def menu_student(self):
        while True:
            type = int(input('МЕНЮ УЧАЩЕГОСЯ: ' '\n' '1. Поиск личной информации' '\n' 
                              '2. Поиск информации, по всем студентам' '\n' '0. Выход' '\n'
                              'Выберите категорию(введите цифру): '))
            if type == 1:
                my_info = DataBase()
                data = my_info.search_personal_infoS(self.login)
                print(data['status'],':', data['name'], data['surname'], '\n' 'Курс: ', data['course'],'\n'
                      'Математика: ', data['maths'],'\n' 'Физика: ', data['physics'],'\n'
                      'Информатика: ', data['informatics'], '\n''Литература: ', data['literature'],'\n'
                      'Философия: ', data['philosophy'],'\n' 'Средний балл: ', data['average_ball'])

            elif type == 2:
                my_info = DataBase()
                my_info.search_general_infoS()

            elif type == 0:
                break

            else:
                print('Выберите пункт')
