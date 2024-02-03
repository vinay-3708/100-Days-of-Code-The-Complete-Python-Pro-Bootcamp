print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_pge = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = bill + ( bill * tip_pge / 100 )
split_bill = total / people
print(f"Each person should pay: ${split_bill:.2f}")