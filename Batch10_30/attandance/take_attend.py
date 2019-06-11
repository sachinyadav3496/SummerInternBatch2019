import time

date = time.strftime("%d/%m/%Y")

fp = open("attendance.csv")
line  = fp.readline().strip('\n')

new_data = line+","+date+'\n'
c = 1 
for line in fp : 
    line = line.strip('\n')
    if line : 
        name = line.split(',')[0]
        present = input(f"{c}. {name}  : ")
        if present : 
            present = "A"
        else : 
            present = "P"
        new_data += line+","+present+"\n"
    c += 1
else : 
        fp.close()

fp = open("attendance.csv","w")
fp.write(new_data)
fp.close()

