#part I

students = [
     {'first_name': 'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
]


def people_listed(x):
    for i in range(len(x)):
        temp_dict = students[i]
        y = ""
        x = ""
        for key in temp_dict:
            y = temp_dict[key] + " "
            x = x + y
        print x

people_listed(students)

#part 2

users = {
 'Students': [
     {'first_name': 'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }


def people_listed1(z):
    for key1 in z:
        print key1
        person = z[key1]
        count = 0
        for i in range(len(person)):
            temp_dict = person[i]
            y = ""
            x = ""
            for key in temp_dict:
                y = temp_dict[key]
                x = x + " " + y
            count += 1
            print str(count) + " -" + x + " - " + str(len(x) - 2)

people_listed1(users)