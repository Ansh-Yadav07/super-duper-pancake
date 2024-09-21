print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_value=((tip/100) *bill)  #percentage to integer
total_bill=tip_value+bill
bill_per_person=round((total_bill/people),3)
print('Each person have to Pay',bill_per_person)


