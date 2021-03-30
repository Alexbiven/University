import pymysql
from pymysql.cursors import DictCursor


class Student:

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

    def search_information(self):
        sql = "SELECT * FROM human"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        for element in data:
            if element['surname'] == 'Petrov':
                print( 'Имя:',element['name'],'\n''Статус:',element['status'],'\n''Курс:',element['course'],'\n'
                        'Факультет:',element['faculty'],'\n''Оценка:',element['assessment'],'\n'
                        'Средний бал:',element['average_ball'])



# my_Student = Student()
# my_Student.search_information()