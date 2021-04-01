from DataBase import DataBase

class Student:

    def menu_student(self):
        while True:
            type  = int(input('МЕНЮ УЧАЩЕГОСЯ: ' '\n' '1. Поиск личной информации' '\n' 
                              '2. Поиск информации, по всем студентам' '\n' 'Выберите категорию: '))
            if type == 1:
                my_info = DataBase()
                my_info.search_personal_info(input('Введите имя: '), input('Введите фамилию: '))
                #break
            elif type == 2:
                my_info = DataBase()
                my_info.search_general_info()
                #break
            else:
                print('Выберите пункт')

