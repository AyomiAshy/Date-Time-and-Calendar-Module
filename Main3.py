h = float(input("Enter hotel cost per day: "))
d = float(input("Enter number of days: "))
p = float(input("Enter plane ticket cost: "))
v = float(input("Enter vehicle rental cost: "))
th = h * d
total = th + p + v
print("Total trip expenditure: ", total)