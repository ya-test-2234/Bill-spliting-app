import math

def split_check(total, num_of_people): 
	
	if num_of_people != int(num_of_people):
		raise ValueError ("people cannot be fragmented")
	
	if num_of_people <=1: 
		raise ValueError ("more than one persone is required to split the bill") 
	
	if total <=0: 
		raise ValueError ("Bill cannot be negative or zero")
		
	return math.ceil (total / num_of_people) 

rerun = 0

while rerun != "no":

	try: 
		
		while True:
			
			total_due = float(input("Please enter the total: "))
			if total_due != float(total_due):
				print("please enter a number")
				continue
			for_tipping_total = total_due
			
		
			while True:
			
				total_persons = float(input("For how many people? "))
				if total_persons != float(total_persons):
					print("please enter a number")
					continue
				for_tipping_persons = total_persons
				break
			break
		
		amount_due = split_check(total_due,total_persons) 
		
		tip = float((amount_due*for_tipping_persons)-for_tipping_total)
		tip_rounded= "{:.2f}".format(tip) #makes the "tip" float prints to two decimal places
		
	except ValueError as err: 
		print ("please enter a valid value")
		print ("({})".format(err))
		continue
	
		
	else: 
		print("Each person owes ${}".format(amount_due),  "and the tip will be ${}".format(tip_rounded))
		
	rerun = input("would you like to split another bill?(yes/no) ")

else:
	print ("thank you for using our app")