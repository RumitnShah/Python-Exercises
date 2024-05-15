# To verify if file is created of not

#-------------------- Q1 -----------------------
import os

print(os.listdir())  # To call all directories

print(os.path.isfile("Records 22-23"))    #To check if this file is present in directories


#-------------------- Q2 ----------------------
print(os.listdir(r"C:\Users\Administrator\Documents\GitHub\Python-Exercises"))  # To call all directories

print(os.path.isfile(r"C:\Users\Administrator\Documents\GitHub\Python-Exercises\File-Handling\Budget 23-24.txt"))    #To check if this file is present in directories