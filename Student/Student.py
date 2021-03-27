from Human import Human

class Student(Human):

    def __init__(self,name,surname,status, course,faculty,assessment,average_ball):
        Human.__init__(self,name,surname,status)
        self.course = course
        self.faculty = faculty
        self.assessment = assessment
        self.average_ball = average_ball

my_Student = Student('Олег','Петров','Студент','4','Психология','8','4.0')
my_Student.create()
print('Имя: ' + my_Student.name,'\n' 'Фамилия: ' + my_Student.surname,'\n' 'Статус: ' + my_Student.status,
      '\n' 'Курс: ' + my_Student.course, '\n' 'Факультет: ' + my_Student.faculty,'\n' 'Оценка: ' + my_Student.assessment,
      '\n' 'Средний бал: ' + my_Student.average_ball)
