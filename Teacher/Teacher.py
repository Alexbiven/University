import pymysql
from pymysql.cursors import DictCursor


class Teacher:


    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='biven',
            password='11T32cS1',
            db='university',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def edit_information(self,course,faculty,assessment, average_ball):
        sql = "UPDATE human " \
              "SET course = %s, faculty = %s, assessment = %s, average_ball = %s " \
              "WHERE name = 'Igor' and surname = 'Petrov' "
        temp = [ course,faculty,assessment, average_ball]
        self.cursors.execute(sql, temp)
        self.connection.commit()

# my_Teacher = Teacher()
# my_Teacher.edit_information(int(input('Введите номер курса: ')) ,input('Введите название факультета: '),
#                             int(input('Введите оценку: ')), float(input('Введите средний бал: ')))