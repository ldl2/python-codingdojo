#in retrospect there was an easier way but eh
#prints odd numbers
for i in range(1, 1001):
    if i % 2 == 0:
        pass
    else:
        print(i)
#prints multiples of 5
for i in range(1, 1001):
    if i % 5 == 0:
        print(i)

a = [1, 2, 5, 10, 255, 3]

#they are the same list so the same
#can be used to find the average
sum1 = 0
for i in range(len(a)):
    sum1 = a[i] + sum1
    ave = sum1 / len(a)
print("list sum: ", sum1)
print("list average: ", ave)
