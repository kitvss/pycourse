#enter the concert. if you are <18, you can't enter. if you are 18-21, you can enter but can't drink. if you're 21+ you can enter and drink alco

age = input("Please, enter your age: \n")
#we are receiving str in input, so it should be int()
#but i put it in the conditional because int can't be blank
#age = int(age)
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print(f"hi, your age is {age}, this means you can enter the concert, but can't drink alcohol")
	elif age >= 21:
		print(f"hi, your age is {age}, you can enter the concert and enjoy the bar")
	else:
		print(f"hi, your age is {age}, you are too young to be here")
else:
	print("there is no info in input")