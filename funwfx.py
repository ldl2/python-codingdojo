#odd even challenge this is really just calling a for loop
def odd_even():
    for i in range(2001):
        if i % 2 == 0:
            print "Number is " + str(i) + ".  This is an even number"
        else:
            print "Number is " + str(i) + ".  This is an odd number"

odd_even()

#begins multiply function this is just creating your own list
a= []
y = ""
print "'end' finishes list"
while(y != "end"):
    y = raw_input("enter List: ")
    if(y == "end"):
        break
    try:
        a.append(float(y))
    except:
        print("They should be numbers")

#this gets the other variable of the multiply function
num = raw_input("what shall we multiply by:")

#here is the guts of the multiply function note variables aren't intuitive ones
#set elsewhere becuase you need it in multiple cases


def multiply(x, y):
    b = []
    for i in range(len(x)):
        b.append(x[i] * float(y))
    return b
#calls and prints multiply function
mul=multiply(a, num)
print mul


#hackers challenge not too bad basically set a number as while condiitonal and add ones


def layered_multiples(arr):
    new_array = []
    for i in range(len(arr)):
        l1 = []
        while(arr[i] > len(l1)):
            l1.append(int(1))
        new_array.append(l1)
    return new_array

#calls hacker's challenge and prints'
x = layered_multiples(multiply([2, 4, 5], 3))
print x

