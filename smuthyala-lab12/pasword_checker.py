'''Recursion program to check for password validity
Author: Sanjay Reddy Muthyala
'''

def main():
	print("==============>> Password Checker <<===================")
	print("password -- abced1234")
	print("valid: ",does_password_pass_check("abced1234"))
	print("password -- abcderf@1232")
	print("valid: ",does_password_pass_check("abcderf@1232"))
	print("password -- abcedsdsed")
	print("valid: ",does_password_pass_check("abcedsdsed"))
	print("password -- qwsbcndi@1$*")
	print("valid: ",does_password_pass_check("qwsbcndi@1$*"))
	

def does_password_pass_check(password):
	if len(password) == 0:
		return False
	elif password[0].isdigit():
		return True
	else:
		return does_password_pass_check(password[1:])

main()
