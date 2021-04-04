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
            print('There is no such user')
            my_info = DataBase()
            my_info.search_personal_info(input('Введите имя: '),input('Введите фамилию: '))

    def search_general_info(self):
        sql = "SELECT * FROM progress "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        for user in data:
            print('Имя: ',user['name'],'Фамилия: ',user['surname'],'Курс: ',user['course'],
                  'Математика: ',user['maths'],'Физика: ',user['physics'],
                  'Информатика: ',user['informatics'],'Литература: ',user['literature'],
                  'Философия: ',user['philosophy'],'Средний балл: ',user['average_ball'])

    def edit_information(self,surname,name,maths,physics,informatics,literature,philosophy):
        sql = "UPDATE progress" \
              " SET maths = %s, physics = %s, informatics = %s, literature = %s, philosophy = %s" \
              " WHERE surname = '%s' and name = '%s'"
        temp = [surname,name,maths,physics,informatics,literature,philosophy]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def average_ball(self):
        sql = "UPDATE progress SET average_ball = (maths+physics+informatics+literature+philosophy)/5;"
        self.cursors.execute(sql)
        self.connection.commit()


