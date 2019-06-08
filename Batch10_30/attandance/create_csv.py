f = open("attendance.csv","w")
heading = "name"
c = 1
data = heading+"\n"
while not input() : 
    name = input(f"Student[{c}] : ")
    data += name+"\n"
    c += 1
else : 
    f.write(data)
    f.close()
