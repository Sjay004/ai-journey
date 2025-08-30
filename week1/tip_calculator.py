#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator")
bill = float(input("what was your total bill? $"))
tip = int(input("what percentage tip would you like to give ? 10,12,or 15? "))
people = int(input("How many people will you split the bill with ? "))
total = (bill / people) * (1 + tip/100)
final_answer = (round(total,2))
final_answer = "{:.2f}".format(total)
print(f"Each person should pay ${final_answer}")