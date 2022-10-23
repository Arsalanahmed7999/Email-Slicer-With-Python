# Email slicer
# arsalanahmed7999@gmail.com 
# your username is arsalanahmed7999 and your domain is gmail.com

email = input('Enter Your Email: \n')
indexOfa = email.index('@')
username = email[0:indexOfa]
domain = email[indexOfa+1:]
print(f'Your username is {username} and your domain is {domain}')

