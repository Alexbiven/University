# def edit_information(self,course,faculty,assessment, average_ball):
    #     sql = "UPDATE human " \
    #           "SET course = %s, faculty = %s, assessment = %s, average_ball = %s " \
    #           "WHERE name = 'Igor' and surname = 'Petrov' "
    #     temp = [ course,faculty,assessment, average_ball]
    #     self.cursors.execute(sql, temp)
    #     self.connection.commit()

# my_Teacher = Teacher()
# my_Teacher.edit_information(int(input('Введите номер курса: ')) ,input('Введите название факультета: '),
#                             int(input('Введите оценку: ')), float(input('Введите средний бал: ')))


def edit_information(self, surname, name, maths, physics, informatics, literature, philosophy):
    sql = "UPDATE progress" \
          " SET maths = %s, physics = %s, informatics = %s, literature = %s, philosophy = %s" \
          " WHERE surname = 'Pisarev' and name = 'Alexandr'"
    temp = [surname, name, maths, physics, informatics, literature, philosophy]
    self.cursors.execute(sql, temp)
    self.connection.commit()