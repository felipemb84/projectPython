#RANGE()
# mylist = [1,2,3]

# for num in range(0,11,2):
#	print(num)
# range(start, end-not included, steps), just the parameter end is necessary

# list(range(0,11,2))

#ENUMERATE()
# index_count = 0

# for letter in 'abcde':
# 	print('at index {} the letter is {}'.format(index_count, letter))
#	index_count += 1
	
# word = 'abcde'

# for item in enumerate(word):
#	 print(item)
	
# for index, letter in enumerate(word):
# 	print(index)
# 	print(letter)
# 	print('\n') # goes to the next line
	
#ZIP()
# mylist1 = [1,2,3]
# mylist2 = ['a', 'b', 'c']

# for item in zip(mylist1, mylist2): # if u run only zip() u get a message saying that u have a zip waiting for u at a location on your memory, so u can do a for loop
# 	print(item)
# zip will only be able to go as far as the shortest item

# if u just wanna get the list...
# list(zip(mylist1, mylist2))

#IN
# 2 in [1,2,3]
# 'x' in ['x', 'y', 'z']
# 'a' in 'a world'
# 'mykey' in {'mykey':345}
# checks if something is inside some other thing

#MIN and MAX
# min(mylist)
# max(mylist)

#SHUFFLE from random
# from random import shuffle
# mylist = [1,2,3,4,5,6,7,8,9,10]
# shuffle(mylist)

#RANDINT from random
# from random import randint
# randint(0,100) # return back a interger between 0, 100

#INPUT
# input('Enter a number here ')

# result = input('What is your name? ')
# print(result)
