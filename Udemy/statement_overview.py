st1 = 'Sam Print only the words that start with s in this sentence'

for word in st1.split():
	if word[0].lower() == 's':
		print(word)
		
		
for num in range(0,11,2):
	print(num)
	

print([x for x in range(1,51) if x%3 == 0 ])


st2 = 'Print word in this sentence that has an even number of letters'

for word in st2.split():
	if len(word) % 2 == 0:
		print(word+ ' is even!')
		

for num in range(1,101):
	if num%3 == 0 and num%5 == 0:
		print('FizzBuzz')
	elif num%3 == 0:
		print('Fizz')
	elif num%5 == 0:
		print('Buzz')
	else:
		print(num)
		
		
st3 = 'Create a list of the first letters of every word in this string'
	
print([word[0] for word in st3.split()])
