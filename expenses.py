expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = 0


print("You spent $", total, " on lunch this week.")

numExpenses = int(input("Enter # of expenses:"))
for i in range(numExpenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total)
