# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A= sorted(A)
    print A
    l = len(A)
    if A[0] > 0:
        for i in range(l - 1):
            print A[i], i
            print A[i + 1],  A[i] + 1
            if A[i] != A[i + 1] and A[i] + 1 != A[i + 1]:
                return A[i] + 1
    else:
        return abs(A[0])

if __name__ == '__main__':
    print solution([1, 3, 6, 4, 1, 2])