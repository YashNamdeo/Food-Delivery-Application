#All user services reside here

import os
import datetime
from hotel_services import give_hotel_details, view_profile, give_dish_details, view_dish

hotel_list, hotel_profile,hotel_name_id = give_hotel_details()
dish_list = give_dish_details()
user_list=[]
user_profile={}
user_order_list={}

def generate_profile(user_id):
	name = str(input("Please enter your name: ")).lower()
	mob = str(input("Please enter your contact no: ")).lower()
	address = str(input("Please enter your address: ")).lower()
	list1=[name,mob,address]
	user_profile[user_id]=list1
	user_order_list[user_id]={}
	print("Profile has been created successfully :)")
	return


def update_profile(user_id):
	print("What do you want to update?"                            
              "\t(M) Contact No\n"     				#name should not be updatable
              "\t(A) Address\n"
              "\t(B) Both\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	if input_1=='M':
		input_2 = str(input("Please enter new contact no: ")).lower()
		user_profile[user_id][1]=input_2
	elif input_1=='A':
		input_2 = str(input("Please enter new address: ")).lower()
		user_profile[user_id][2]=input_2
	elif input_1 == 'B':
		input_2a = str(input("Please enter new contact no: ")).lower()
		user_profile[user_id][1]=input_2a
		input_2b = str(input("Please enter new address: ")).lower()
		user_profile[user_id][2]=input_2b
	else:
		print("ERROR: Invalid Input, please try again!")
	print("Profile updated successfully :)")
	return


def view_profile_user(user_id):
	if user_id in user_profile:
		print("Name:" + user_profile[user_id][0])
		print("Contact No:" + user_profile[user_id][1])
		print("Address:" + user_profile[user_id][2])
	else:
		print("Haven't yet registered \n")
	return

def delete_profile(user_id):
	del user_profile[user_id]
	user_list.remove(user_id)
	print("Account removed successfully :|")
	return

def search_hotel():
	name = str(input("Please enter the hotel you want to search: ")).lower()
	if name in hotel_list:
		l=view_profile(hotel_name_id[name])
		if l==-1:
			search_hotel()
		else:
			name_1 = str(input("Please select: ")).lower()
			return name,name_1
	else:
		print("ERROR: Invalid Input, please try again!")
		search_hotel()

def search_dishes():
	print("Please select what do you want to search:\n"                            
              "\t(M) Main Course\n"     				#name should not be updatable
              "\t(A) Appetizer\n"
              "\t(D) Dessert\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	if input_1=='M':
		view_dish('main course')
		name_1 = str(input("Please select: ")).lower()
		return name_1
	elif input_1 =='A':
		view_dish('appetizer')
		name_1 = str(input("Please select: ")).lower()
		return name_1
	elif input_1=='D':
		view_dish('dessert')
		name_1 = str(input("Please select: ")).lower()
		return name_1
	else:
		print("ERROR: Invalid Input, please try again!")
		search_dishes()

def place_order(user_id):
	x = datetime.datetime.now()
	user_order_list[user_id][x]=[]
	print("Please enter your choice: \n"
              "\t(A) Search by food name\n"                              
              "\t(B) Search by hotel name\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	if input_1 == 'A':
		user_order_list[user_id][x].append(search_dishes())
	elif input_1 == 'B':
		hotel,dish=search_hotel()
		if hotel_profile[hotel_name_id[hotel]][5]+1 <= hotel_profile[hotel_name_id[hotel]][3]:
			user_order_list[user_id][x].append(dish)
			hotel_profile[hotel_name_id[hotel]][5]+=1
		else:
			print("Unable to make order, capacity full")
			print("Try again")
			place_order(user_id)
	else:
		print("ERROR: Invalid Input, please try again!")
		place_order(user_id)
	return x

def previous_order(user_id):
	if user_id in user_order_list:
		print_order(user_order_list[user_id])
	else:
		print("Haven't ordered yet \n")
	return


def print_order(dct):
    print("Time : Order")
    for item, amount in dct.items():  
        print("{} : {}".format(item, amount))


def order_status(user_id, x):
	d1 = datetime.datetime.now()
	if d1 > x+datetime.timedelta(minutes = 30):
		print("Success: Order Deleivered")
	elif d1 > x+datetime.timedelta(minutes = 20):       #when order dispatch then the no of orders with hotel decrease
		print("Order dispatched")
		hotel_profile[user_id][5]-=1
	elif d1 > x+datetime.timedelta(minutes = 10):
		print("Order getting ready")
	else:
		print("Success: order placed")
	return

cur_time=datetime.datetime.now()
def actions(user_id):
	print("\nActions:\n "
	              "\t(O) Place Order\n"                              
	              "\t(P) Previous Orders\n"
	              "\t(S) Order Status\n"
	              "\t(U) Update Profile\n"
	              "\t(V) View Profile\n"
	              "\t(D) Delete Profile\n"
	              "\t(E) Exit\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	global cur_time
	if input_1 == 'O':
		cur_time=place_order(user_id)
	elif input_1 == 'P':
		previous_order(user_id)
	elif input_1 == 'U':
		update_profile(user_id)
	elif input_1 == 'V':
		view_profile_user(user_id)
	elif input_1 == 'D':
		delete_profile(user_id)
	elif input_1 == 'S':
		order_status(user_id,cur_time)
	elif input_1 == 'E':
		return
	else:
		print("ERROR: Invalid Input, please try again!") 

	actions(user_id)


def user():
	print("Are you an existing user or new user? \n"
	              "\t(E) Existing User\n"                              
	              "\t(N) New User\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	input_2=None
	if input_1=='E':
		input_2 = str(input("Please enter your mail id: ")).lower()
		if input_2 not in user_list:
			print("Account doesn't exist, please create a new one :)")
	elif input_1=='N':
		input_2 = str(input("Please enter your mail id: ")).lower()
		user_list.append(input_2)
		generate_profile(input_2)
	else:
		print("ERROR: Invalid Input, please try again!")
		user()

	actions(input_2)
