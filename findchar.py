word_list = []
y = ""
print "'end' finishes list"
while(y != "end"):
    y = raw_input("enter List 1: ")
    if(y == "end"):
        break
    try:
        word_list.append(float(y))
    except:
        word_list.append(y)

letter = raw_input("enter 1 letter (case sensitive):")

new_list = []
for i in range(len(word_list)):
    word = word_list[i]
    for i in range(len(word)):
        if letter == word[i]:
            new_list.append(word)
        else:
            pass
print new_list