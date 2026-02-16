
# Expenses for each month from January to May

Expenses = [2200, 2350, 2600, 2130, 2190]  # January, February, March, April, May




# Calculate extra money spent in February compared to January

Extra_spent_feb = Expenses[1] - Expenses[0]
print(Extra_spent_feb)





Total_expense_of_quarter = sum(Expenses[0:3])
print(Total_expense_of_quarter)






if 2000 in Expenses:
    print("Yes 2000 is spend")
else:
    print("No, 2000 was not spent in any month")





Expenses.append(1980)
print(Expenses)






Expenses[3] = Expenses[3] - 200
print(Expenses)
