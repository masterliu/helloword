# -*- coding: UTF-8 -*-
letter = str(raw_input('input:'))
# letter=letter1.upper()
# print letter
if letter == 'S':
	print ('you need input second letter:')
	letter = input('input:')
	if letter == 'a':
		print ('saturday')
	elif letter == 'u':
		print ('sunday')
	else:
		print ('error')
elif letter == 'F':
	print ('friday')
elif letter == 'M':
	print ('monday')

elif letter == 'T':
	print ('you need input second letter:')
	letter = input('input:')

	if letter == 'u':
		print ('Tuesday')
	elif letter == 'h':
		print ('Thursday')
	else:
		print ('error')
elif letter == 'W':
	print ('Wednesday')
else:
	print ('error')
