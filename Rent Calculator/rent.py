# A simple rent calculator

room_No = int(input("Enter your Hostel/Flat number: "))
rent = int(input("Enter your Hostel/Flat rent: "))
food = int(input("Enter the amount of food ordered: "))
elec_spend = int(input("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the charge per unit: "))
person = int(input("Enter the number of people living: "))

total_bill = elec_spend * charge_per_unit

output = (food + rent + total_bill)

print('Room Number: ',room_No)
print('Total bill: ',output)
print('Total bill for per persons: ',output//person)
