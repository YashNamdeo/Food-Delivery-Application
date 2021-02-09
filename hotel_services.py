#All hotel services reside here

import os
import datetime

hotel_list=[]
hotel_profile={}
dishes_list={}
dishes_list['main course']=[]
dishes_list['appetizer']=[]
dishes_list['dessert']=[]
main_list={}
appe_list={}
desse_list={}
hotel_name_id={}

def give_hotel_details():
	return hotel_list, hotel_profile,hotel_name_id

def give_dish_details():
	return dishes_list

def print_hotel(dct):
    print("Items : value")
    for item, amount in dct.items():  
        print("{} : {}".format(item, amount))

def print_dishes(dct):
    print("Item: Information")
    for i in dct:
        print("{} : {}".format(i[0], [i[1],i[2]]))


def generate_profile(user_id,name):
	#name = str(input("Please enter the Restuarant name: ")).lower()
	mob = str(input("Please enter the contact no: ")).lower()
	address = str(input("Please enter the address: ")).lower()
	n = int(input("Please enter the maximum processing capacity: (Integer value only) "))
	print("Please enter your menu: ")
	x = int(input("No of contents in menu: "))
	iterms={}
	while x!=0:
		print("Please select what you want to add:\n"                            
              "\t(M) Main Course\n"     				#name should not be updatable
              "\t(A) Appetizer\n"
              "\t(D) Dessert\n")
		input_1 = str(input("Please Select Your Operation: ")).upper()
		if input_1 == 'M':
			itm = str(input("Please enter the content: ")).lower()
			pr=int(input("Please enter " + itm + " price: (Integer value only) "))
			iterms[itm]=pr
			o=len(dishes_list['main course'])
			dishes_list['main course'].append([itm,pr,user_id])
			main_list[itm]=o
		elif input_1 == 'A':
			itm = str(input("Please enter the content: ")).lower()
			pr=int(input("Please enter " + itm + " price: (Integer value only) "))
			iterms[itm]=pr
			o=len(dishes_list['appetizer'])
			dishes_list['appetizer'].append([itm,pr,user_id])
			appe_list[itm]=o
		elif input_1 == 'D':
			itm = str(input("Please enter the content: ")).lower()
			pr=int(input("Please enter " + itm + " price: (Integer value only) "))
			iterms[itm]=pr
			o=len(dishes_list['dessert'])
			dishes_list['dessert'].append([itm,pr,user_id])
			desse_list[itm]=o
		else:
			print("ERROR: Invalid Input, please try again!")
			x+=1
		x-=1
	k=0
	list1 = [name,mob,address,n,iterms,k]
	hotel_profile[user_id]=list1
	print("Profile has been created successfully :)")
	return


def update_profile(user_id):      ###price and list not in sync need to modify it
	if user_id in hotel_profile:
		print("What do you want to update\n"                        
              "\t(M) Contact No\n"     				#name should not be updatable
              "\t(A) Address\n"
              "\t(B) Both\n"
              "\t(C) Content\n")
		input_1 = str(input("Please Select Your Operation: ")).upper()
		if input_1=='M':
			input_2 = str(input("Please enter new contact no: ")).lower()
			hotel_profile[user_id][1]=input_2
		elif input_1=='A':
			input_2 = str(input("Please enter new address: ")).lower()
			hotel_profile[user_id][2]=input_2
		elif input_1=='B':
			input_2a = str(input("Please enter new contact no: ")).lower()
			hotel_profile[user_id][1]=input_2a
			input_2b = str(input("Please enter new address: ")).lower()
			hotel_profile[user_id][2]=input_2b
		else:
			print("What do you want to update? \n"                            
	              "\t(A) Add new content\n"     				#name should not be updatable
	              "\t(P) Update price\n"
	              "\t(R) Remove content\n")
			input_1a  = str(input("Please Select Your Operation: ")).upper()
			if input_1a == 'A':
				iterms=hotel_profile[user_id][4]
				print("Please select what you want to add:"                            
	              "\t(M) Main Course\n"     				#name should not be updatable
	              "\t(A) Appetizer\n"
	              "\t(D) Dessert\n")
				input_1_c = str(input("Please Select Your Operation: ")).upper()
				itm = str(input("Please enter the new content: ")).lower()
				pr=int(input("Please enter" + itm + "price: (Integer value only) "))
				iterms[itm]=pr
				hotel_profile[user_id][4]=iterms
				if input_1_c=='M':
					o=len(dishes_list['main course'])
					dishes_list['main course'].append([itm,pr,user_id])
					main_list[itm]=o
				elif input_1_c=='A':
					o=len(dishes_list['appetizer'])
					dishes_list['appetizer'].append([itm,pr,user_id])
					appe_list[itm]=o
				else:
					o=len(dishes_list['dessert'])
					dishes_list['dessert'].append([itm,pr,user_id])
					desse_list[itm]=o
			elif input_1a == 'P':
				print("Please select what you want to add:\n"                            
	              "\t(M) Main Course\n"     				#name should not be updatable
	              "\t(A) Appetizer\n"
	              "\t(D) Dessert\n")
				input_1_c = str(input("Please Select Your Operation: ")).upper()
				itm = str(input("Please enter the content: ")).lower()
				pr=int(input("Please enter" + itm + "new price: (Integer value only) "))
				hotel_profile[user_id][4][itm]=pr
				if input_1_c=='M':
					o=main_list[itm]
					dishes_list['main course'][o][1]=pr
				elif input_1_c=='A':
					o=appe_list[itm]
					dishes_list['appetizer'][o][1]=pr
				else:
					o=desse_list[itm]
					dishes_list['dessert'][o][1]=pr
			else:
				print("Please select what you want to add:\n"                            
	              "\t(M) Main Course\n"     				#name should not be updatable
	              "\t(A) Appetizer\n"
	              "\t(D) Dessert\n")
				input_1_c = str(input("Please Select Your Operation: ")).upper()
				itm = str(input("Please enter the content to remove: ")).lower()
				iterms=hotel_profile[user_id][4]
				del iterms[itm]
				hotel_profile[user_id][4]=iterms
				if input_1_c=='M':
					o=main_list[itm]
					del dishes_list['main course'][o]
					del main_list[itm]
				elif input_1_c=='A':
					o=appe_list[itm]
					del dishes_list['appetizer'][o]
					del appe_list[itm]
				else:
					o=desse_list[itm]
					del dishes_list['dessert'][o]
					del desse_list[itm]

		print("Profile updated successfully :)")
	else:
		print("Hotel doesn't exist \n")
	return


def view_profile(user_id):
	if user_id in hotel_profile:
		print("Name:" + hotel_profile[user_id][0])
		print("Contact No:" + hotel_profile[user_id][1])
		print("Address:" + hotel_profile[user_id][2])
		#print("Order Contraints:" + hotel_profile[user_id][3])
		#print("Current Orders:" + hotel_profile[user_id][5])
		print("\n Food Menu:")
		print_hotel(hotel_profile[user_id][4])
	else:
		print("Hotel doesn't exist \n")
	return


def view_dish(name):    ###need to done
	if name in dishes_list:
		print("List of items:")
		print_dishes(dishes_list[name])
	else:
		print("Dish doesn't exist \n")
	return


def delete_profile(user_id):
	if user_id in hotel_profile:
		hotel_list.remove(hotel_profile[user_id][0])
		del hotel_profile[user_id]
		print("Account removed successfully :|")
	else:
		print("Account Doesn't exist")
	return


def actions(user_id):
	print("Actions:\n "
	              "\t(O) Update Profile\n"                              
	              "\t(P) View Profile\n"
	              "\t(S) Delete Profile\n"
	              "\t(E) Exit\n")
	input_1 = str(input("Please Select Your Operation: ")).upper()
	if input_1 == 'O':
		update_profile(user_id)
	elif input_1 == 'P':
		view_profile(user_id)
	elif input_1 == 'S':
		delete_profile(user_id)
	elif input_1 == 'E':
		return
	else:
		print("ERROR: Invalid Input, please try again!") 

	actions(user_id)

def hotel():
	print("Are you an existing user or new user? \n"
	              "\t(E) Existing User\n"                              
	              "\t(N) New User\n")

	input_1 = str(input("Please Select Your Operation: ")).upper()
	input_2=None
	if input_1=='E':
		input_2 = str(input("Please enter your mail id: ")).lower()
		name = str(input("Please enter the Restuarant name: ")).lower()
		if name not in hotel_list:
			print("Account doesn't exist, please create a new one :)")
		hotel()
	elif input_1=='N':
		input_2 = str(input("Please enter your mail id: ")).lower()
		name = str(input("Please enter the Restuarant name: ")).lower()
		hotel_list.append(name)
		generate_profile(input_2,name)
		hotel_name_id[name]=input_2
	else:
		print("ERROR: Invalid Input, please try again!")
		hotel()

	actions(input_2)
