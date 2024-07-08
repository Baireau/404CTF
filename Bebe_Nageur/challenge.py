from flag import FLAG
import random as rd

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def f(a,b,len_charset,x):
    #print((a*x+b)%len_charset)
	return (a*x+b)%len_charset

def encrypt(message,a,b,len_charset):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f(a,b,len_charset,x)
		encrypted += charset[x]

	return encrypted

len_charset = len(charset)
a = rd.randint(2,len_charset-1)
b = rd.randint(1,len_charset-1)

print(encrypt(FLAG,a,b,len_charset))

# ENCRYPTED FLAG : -4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_
