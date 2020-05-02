class Student:
    def __init__(self, roll, name, city, mobile):
        self.roll = roll
        self.name = name
        self.city = city
        self.mobile = mobile

    def studying(self):
        print self.name + " is studying !!"

    def print_student(self):
        print self.__dict__


if __name__ == '__main__':
    student1 = Student(11, "ram", "pune", 3321321321)
    student1.studying()
    student1.print_student()
