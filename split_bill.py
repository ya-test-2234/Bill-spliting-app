import math


def get_amount_due ():
	
	while True:
		try: 
			total = float(input("Enter total: "))
		
			while total <= 0:
				total = float(input("\nBill cannot be negative or zero, please enter a valid amount: "))
		
		except ValueError:
			print("\nPlease enter a valid amount")
			continue
		break
		
	while True:
		try: 
			num_persons = float(input("\nEnter total persons: "))
		
			while num_persons <= 1 or num_persons != int(num_persons):
				num_persons = float(input("\nPlease enter a correct number of people: "))
		
		except ValueError:
			print("\nPlease enter a valid number")
			continue
		break
		
	amount_due = math.ceil (total/num_persons)
	
	change = amount_due * num_persons - total
		
	return amount_due, change #returns tuple

rerun = 'yes'
while rerun.lower() == 'yes':
	
	amount_due, change = get_amount_due() #unpack tuple
	
	print(f"\nEach person owes {amount_due}$ and the change will be {change:.2f}$\n")
	
	rerun = input("Would you like to split another bill? [Yes/No]\n") 
	
	while rerun.lower() != 'yes' and rerun.lower() != 'no': #coarse valid input
	
		rerun = input("Would you like to split another bill? [Yes/No]\n")

print ("thank you for using our app")
