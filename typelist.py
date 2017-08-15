new_dct = {
    "l1": [2, 3, 1, 7, 4, 12],
    "l2": ['magical', 'unicorns'],
    "l3": ['magical unicorns', 19, 'hello', 98.98, 'world'],
}



list1 = raw_input("enter test case (1-3) or make 4: l1, l2, l3, l4: ")

if(list1 == "l4"):
    print("end exits")
    listmaker = ""
    newlist = []
    while(listmaker != "end"):
        listmaker = raw_input("list input: ")
        if(listmaker == "end"):
            break
        try:
            newlist.append(float(listmaker))
        except:
            newlist.append(listmaker)
        print(newlist)
    new_dct["l4"] = newlist
else:
    pass

x = new_dct.get(list1)

sum1 = 0
words = ""

for i in range(len(x)):
    if(type(x[i]) == int or type(x[i]) == float):
        sum1 = x[i] + sum1
        if(sum1 == 0):
            break
    else:
        words = words + " " + x[i]

if(len(words) > 0):
    if(sum1 != 0):
        print"The list you entered is of mixed type"
        print"Sum: ", sum1
        print"String: ", words
    else:
        print"The list you entered is of string type"
        print"String: ", words
else:
    print"The list you entered is of number type"
    print"Sum: ", sum1