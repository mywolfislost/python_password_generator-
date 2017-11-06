import random
#Author is Akash, find me @mywolfislost
source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+,./;;\[],./`~<>?:"|{}"'
length = input('Length of Password Required ?')
length = int(length)

number = input('How many Passwords Required ?')
number = int(number)
for p in range(number):
 password = ''
 for c in range(length):
  password += random.choice(source)
 print(password)  
