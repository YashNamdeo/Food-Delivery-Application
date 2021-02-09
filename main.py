import os
from user_services import *
from hotel_services import *

print("\n" * 3)      
print("*" * 20 + "Welcome to Mini Swiggy" + "*" * 20)
print("\n" * 3)
hot_cnt=0

def actions():
	global hot_cnt
	print("Are you an Customer or Hotel? \n"
	              "\t(C) Customer\n"                              
	              "\t(H) Hotel\n"
	              "\t(E) Exit\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	if input_1 =='C':
		if hot_cnt==0:
			print("There are no hotels registered :(")
		else:
			user()
			actions()
	elif input_1=='H':
		hot_cnt+=1
		hotel()
		actions()
	else:
		return

actions()
print("Thank for chossing us, Have a nice day!")