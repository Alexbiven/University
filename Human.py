class Human:

    def __init__(self,name,surname,status):
        self.name = name
        self.surname = surname
        self.status = status

    def create(self):
        print('Человек внесен в базу данных')