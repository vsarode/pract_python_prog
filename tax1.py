gender = raw_input("Enter gender (m/f): ")
salary = int(raw_input("Enter your salary: "))
print type(gender)
print type(salary)


if gender=='m':
    if salary>250000:
        print "Apply tax for male!!"
    else:
        print "No tax for male!!"
elif gender=='f':
    if salary>300000:
        print "Apply tax for female!!"
    else:
        print "No tax for female!!"
