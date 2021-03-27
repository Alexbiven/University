from Human import Human

class Teacher(Human):
    def __init__(self,surname,name,middle_name,status):
        Human.__init__(self,name,surname,status)
        self.middle_name = middle_name




my_Teacher = Teacher('Иванова','Татьяна','Николаевна','Преподаватель')
my_Teacher.create()
print('Фамилия: ' + my_Teacher.surname,'\n' 'Имя: ' + my_Teacher.name,'\n' 'Отчество: ' + my_Teacher.middle_name,
      '\n' 'Статус: ' + my_Teacher.status)