def calculate_total_marks(*args):
	print args
	res = 0
	for i in args:
		res += i
	return res


'''
count = input("Enter the count of numbers u want to add: ")
nums = []
for i in range(count):
	val = input("Enter number "+str(i)+" :")
	nums.append(val)
print nums
'''
l  = (10,20,30,40,50,60)
print calculate_total_marks(l)
