def add(*nos):
    # return sum(nos)
    print "data=>", nos
    res = 0
    for no in nos:
        res += no
    return res


#
# def mul(no1, no2=2):
#     return no1*no2

def get_result(rn, **subs):
    return 'Result for roll no=' + str(rn) + "\nNon technical avg=" + str(
        (subs['math'] + subs['eng']) / 2)+"\nTechnical avg="+str((subs['c']+subs['cpp']+subs['java'])/3)


if __name__ == '__main__':
# print add(1,2,3,4,5,6,7)
# print mul(2,10)
# print mul(2)
    print get_result(10, math=40, c=99, eng=50, java=100, cpp=98)
