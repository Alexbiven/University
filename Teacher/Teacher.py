from DataBase import DataBase

class Teacher:

    def menu_teacher(self):
        while True:
            type = int(input('МЕНЮ ПРЕПОДАВАТЕЛЯ: ' '\n' '1. Поиск личной информации, студента' '\n'
                             '2. Поиск информации, по всем студентам' '\n'
                             '3. Редактировать информацию о студентах' '\n' 
                             'Выберите категорию(введите цифру): '))
            if type == 1:
                my_info = DataBase()
                my_info.search_personal_info(input('Введите имя: '), input('Введите фамилию: '))
                #break
            elif type == 2:
                my_info = DataBase()
                my_info.search_general_info()
                #break
            elif type == 3:
                my_info = DataBase()
                my_info.edit_information(input('Введите фамилию: '), input('Введите имя: '),
                                         int(input('Математика: ')), int(input('Физика: ')),
                                         int(input('Информатика: ')),
                                         int(input('Литература: ')), int(input('Философия: ')))
                my_info.average_ball()
                #break
            else:
                print('Выберите пункт')

