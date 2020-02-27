# mystring = 'hello'

# mylist = []

# for letter in mystring:
# 	mylist.append(letter)
	
# OR (flatting out the for loop)

# mylist = [letter for letter in mystring]


mylist2 = [x for x in 'word']

mylist3 = [qweqwe for qweqwe in 'wordtwo']

mylist4 = [num for num in range(0,11)]

mylist5 = [num**2 for num in range(0,11)]

mylist6 = [x for x in range(0,11) if x%2==0]

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(mylist2)
print(mylist3)
print(mylist4)
print(mylist5)
print(mylist6)
print(fahrenheit)

# with if/else statement
results = [x if x%2 else 'ODD' for x in range(0,11)]
