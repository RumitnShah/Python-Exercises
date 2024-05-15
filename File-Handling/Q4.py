# Create a file if it doesn't exist

import os

file_path = r"C:\Users\Administrator\Documents\GitHub\Python-Exercises\File-Handling\Budget 23-24.txt"

if os.path.exists(file_path):
    print("file already exists")

else:
    with open(file_path, 'w') as f1:
        f1.write('This is first line')


#--------------------------------- OR ----------------------------------
        
try:
    file_path = r"C:\Users\Administrator\Documents\GitHub\Python-Exercises\File-Handling\Budget 23-24.txt"
    
    with open(file_path, 'x') as fp:
        pass
    
except:
    print('File already exists')
