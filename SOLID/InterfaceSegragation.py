class Human():
    def __init__(self):
        pass

    def get_data(self):
        raise NotImplementedError


class Student(Human):
    def get_data(self):
        return "data"


if __name__ == '__main__':
    h = Student()
    print h
