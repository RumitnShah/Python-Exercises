# Using different file modes

with open("Records 23-24" , "x") as f1:
    pass

with open("Records 22-23" , "w") as f2:
    f2.write("Budget for this financial year is $9837200")