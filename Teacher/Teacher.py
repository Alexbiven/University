from Human import Human

class Teacher(Human):
    def __init__(self,name,surname,status,middle_name):
        Human.__init__(name,surname,status)
        self.middle_name = middle_name


my_Teacher = Teacher()