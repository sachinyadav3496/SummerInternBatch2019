import sys
import os



if len(sys.argv) > 1 : 
    path = sys.argv[1]
    data = os.listdir(path)
else : 
    data = os.listdir()
    
    
for each_file in data : 
    print(each_file)
