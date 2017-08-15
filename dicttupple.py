my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def dict_tuple(x):
    list1 = []
    for key in x:
        tup = (key, x[key])
        list1.append(tup)
    return list1

y = dict_tuple(my_dict)
print y