#find and replace
words = "It's thanksgiving day.  It's my birthday, too!"
position=words.find("day")
word=words.replace(" day", " month")
print(position)
print(word)

#min and max
x = [2,54,-2,7,12,98]
y=max(x)
z=min(x)
print("max: ", y, "min: ", z)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
y= x[len(x)-1]
z=x[0]
print("first: ", z, "last: ", y)
a=[]
a.append(y)
a.append(z)
print(a)

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y=sorted(x)
z1=y[0:5]
z2=y[5:11]
z3=[]
z3.append(z1)
for i in range(len(z2)):
	z3.append(z2[i])
print(z3)
