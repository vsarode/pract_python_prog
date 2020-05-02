class Mytest():
    def __new__(cls):
        print("new got called")
        return super(Mytest, cls).__new__(cls)

    def __init__(self):
        print("init got called")

    def min_partition_for_palindrom(self):
        return 1,2,3


if __name__ == '__main__':
    c = Mytest()
    j,l = c.min_partition_for_palindrom()
    print(j,k)
