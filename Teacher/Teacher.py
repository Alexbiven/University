from DataBase import DataBase



class Teacher:

    def menu_teacher(self):
        while True:
            type = int(input('МЕНЮ ПРЕПОДАВАТЕЛЯ: ' '\n' '1. Поиск личной информации, студента' '\n'
                             '2. Поиск информации, по всем студентам' '\n'
                             '3. Редактировать информацию о студентах' '\n' '4. Выход' '\n'
                             'Выберите категорию(введите цифру): '))
            if type == 1:
                my_info = DataBase()
                my_info.search_personal_info(input('Введите имя: '), input('Введите фамилию: '))
                #break
            elif type == 2:
                my_info = DataBase()
                my_info.search_general_infoT()
                #break
            elif type == 3:
                while True:
                    act = int(input('Какую информацию хотите изменить?''\n' '1. Изменить курс' '\n' '2. Изменить успеваемость''\n'
                                    '3. Изменить статус''\n' '4. Выйти в меню преподавателя''\n'
                                    'Выберите пункт(введите цифру): '))
                    if act == 1:
                        my_info = DataBase()
                        my_info.update_course(input('Введите фамилию: '), input('Введите имя: '),
                                                 int(input('Введите номер курса: ')))

                    elif act == 2:
                        list = ['maths', 'physics', 'informatics', 'literature', 'philosophy']
                        print('СПИСОК ДИСЦИПЛИН' '\n' '1:maths 2:physics 3:informatics 4:literature 5:philosophy')
                        point = int(input('Выберите дисциплину,которую хотите изменить(введите цифру): '))
                        discipline = (list[point - 1])
                        my_info = DataBase()
                        my_info.edit_information(input('Введите фамилию: '), input('Введите имя: '),
                                                 discipline, int(input('Оценка: ')))
                        my_info.average_ball()
                        my_Teacher = Teacher()
                        my_Teacher.menu_teacher()

                    elif act == 3:
                        my_info = DataBase()
                        my_info.update_status(input('Введите фамилию: '), input('Введите имя: '),
                                              input('Введите новый статус(Student или Teacher): '))

                    elif act == 4:
                        my_Teacher = Teacher()
                        my_Teacher.menu_teacher()
                    else:
                        my_Teacher = Teacher()
                        my_Teacher.menu_teacher()
            elif type == 4:
                print('Войдите в личный кабинет')


            else:
                print('Выберите пункт')

