# Uses python3
import time
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

if n < 2:
    print('Not a valid input')
elif n == 2:
    result = a[0]*a[1]
else:
    result = 0
    # method1
    start_time = time.time()
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    time1 = (time.time() - start_time)*1000
    print(result)
    print('The time spend on calculation is: ', time1)

    # method 2 of implementation
    start_time2 = time.time()
    p1, p2, n1, n2 = 0, 0, 0, 0
    for i in range(n):
        t = a[i]
        if t > 0:
            if t > p1:
                p2 = p1
                p1 = t
            elif t > p2:
                p2 = t
        else:
            if abs(t) > abs(n1):
                n2 = n1
                n1 = t
            elif abs(t) > abs(n2):
                n2 = t
    result2 = max(p1*p2, n1*n2)
    time2 = (time.time() - start_time2)*1000
    print(result2)
    print('The time spend on calculation is: ', time2)

