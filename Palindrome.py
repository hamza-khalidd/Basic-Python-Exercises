def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('Enter: ')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is not a Palindrome')