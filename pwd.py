#Password retry

password = '123456a?'
i = 3 # The max times u can enter pwd.

while i > 0:
	i = i - 1 
	pwd = input('Please enter your password: ')
	if pwd == password:
		print('login sucess!')
		break
	elif i == 0:
		print('login failed')
	else:
		print('WRONG!! You have ', i, 'times chances')





