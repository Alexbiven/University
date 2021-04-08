import pymysql
from pymysql.cursors import DictCursor


class DataBase:

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

    def search_personal_info(self,name,surname):
        sql = f"SELECT * FROM progress WHERE name = '{name}' and surname = '{surname}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        if data != ():
            user = data[0]
            if user['name'] == name and user['surname'] == surname:
                print('Имя: ', user['name'],'\n''Фамилия: ', user['surname'],'\n'
                      'Курс: ', user['course'],'\n''Математика: ', user['maths'],'\n'
                      'Физика: ', user['physics'],'\n''Информатика: ', user['informatics'],'\n'
                      'Литература: ', user['literature'],'\n''Философия: ', user['philosophy'],'\n'
                      'Средний балл: ', user['average_ball'])
        else:
            print('There is no such User')
            my_info = DataBase()
            my_info.search_personal_info(input('Введите имя: '),input('Введите фамилию: '))

    def search_general_info(self):
        sql = "SELECT * FROM progress "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        for user in data:
            # print('Студент:',user['name'],user['surname'],
            #       'Курс:',user['course'], 'Средний балл:',user['average_ball'])
            print('Студент:',user['name'],user['surname'],'Курс: ',user['course'],
                  'Математика: ',user['maths'],'Физика: ',user['physics'],
                  'Информатика: ',user['informatics'],'Литература: ',user['literature'],
                  'Философия: ',user['philosophy'],'Средний балл: ',user['average_ball'])

    def edit_information(self,surname,name,discipline,mark):
        sql = f"UPDATE progress SET {discipline} = (%s) WHERE surname = (%s) and name = (%s) "
        temp = [mark,surname,name]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def average_ball(self):
        sql = "UPDATE progress SET average_ball = (maths+physics+informatics+literature+philosophy)/5;"
        self.cursors.execute(sql)
        self.connection.commit()


    def update_course(self,surname,name,course):
        sql = f"UPDATE progress SET course = {course} WHERE surname = (%s) and name = (%s)"
        temp = [surname, name]
        self.cursors.execute(sql,temp)
        self.connection.commit()


    def update_status(self,surname,name,status):
        sql = f"UPDATE human,progress SET status = {status} WHERE surname = (%s) and name = (%s)"
        temp = [surname, name]
        self.cursors.execute(sql,temp)
        self.connection.commit()

# my_info = DataBase()
# my_info.update_status(input('Введите фамилию: '), input('Введите имя: '),
#                                               input('Введите новый статус: '))