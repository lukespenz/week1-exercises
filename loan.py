# Get the loan details
moneyOwed = float(
    input("How much money do you owe, in dollars?\n"))  # $50,000
apr = float(input("What is the annual percentage rate?\n"))  # 3%
payment = float(
    input("What will your monthly payment be, in dollars?\n"))  # $1,000
months = int(input("How many months do you want to see results for?\n"))  # 24

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthlyRate = apr/100/12

for i in range(months):
    # Add in interest
    intererstPaid = moneyOwed * monthlyRate
    moneyOwed = moneyOwed + intererstPaid
    if (moneyOwed - payment < 0):
        print("The last payment is", moneyOwed)
        print("You paid off the loan in", i+1, "months")
        break

    # Make payment
    moneyOwed = moneyOwed - payment

    # Print the results after this month
    print("Paid", payment, "of which", intererstPaid, "was interest")
    print("Now I owe", moneyOwed)
