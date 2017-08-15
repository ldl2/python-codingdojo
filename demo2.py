'''
let's print "fizz" when we encounter numbers divvisible by 3 
buzz by 5
fizzbuzz if both
'''

def fizzbuzz():
	#lop from 0 to 100
	for i in range(101):
		#as we lopp check if number is divisible by 3
			if i %3 ==0 and i%5 ==0:
				print("fizzbuzz")
			elif i % 3== 0:
				print("fizz")
			elif i % 5 == 0:
				print("buzz")
			else:
				print(i)


fizzbuzz()