
import os
from datetime import date
class Attendance : 
    def __init__(self,fname):
        Attendance.fname = fname
    def create_file(self):
        fp = open(Attendance.fname,"w")
        s = "Topic Name\nDate"
        c  = 1
        while True : 
            name = input(f"Student[{c}] : ")
            c += 1
            s  = s + "\n" + name.strip().upper()
            if not name :
                s = s[:-1]
                break 
        fp.write(s)
        fp.close()
        print("Data File Exported Sucessfully")
    def update_file(self):
        fp = open(Attendance.fname,"a+")
        c = 1
        while True :  
            name = input(f"Student[{c}] : ").upper().strip()
            last = fp.tell()
            fp.seek(0)
            d = fp.readline()
            fp.seek(last+1) 
            d = len(d.split(","))-1
            c += 1
            if name :
                na = ("NA,"*d)[:-1]
                s = f"\n{name},"+na+"\n"
                fp.write(s)
                
            else : 
                fp.close()
                print("File Exported Sucessfully")
                break
    def take_attendance(self,topic_name):
        print("\nmark A if absent else enter : ")
        fp = open(Attendance.fname)
        dat = date.today()
        line = fp.readline().strip()
        line += f",{topic_name}\n"
        line1 = fp.readline().strip()
        line += line1+f",{dat}\n"
        for newline in fp : 
            newline = newline.strip()
            sname = newline.strip().split(',')[0].title()
            if sname : 
                ch = input(f"{sname} : ").strip().lower()
            else : 
                continue
            if ch :
                line += newline+",A\n"
            else : 
                line += newline+",P\n"
        print("Attendance Taken Sucessfully")
        fp = open(Attendance.fname,"w")
        fp.write(line[:-1])
        fp.close()
            
def main():
    filename = "attendance.csv"
    print("Your Choice : ".center(60))
    print("1. Create New File".center(60))
    print("2. Update Data of Students".center(60))
    print("3. Take Attendance".center(60))
    st = Attendance(filename)
    print("\n\n")
    ch = int(input("Enter your Choice : ".center(60)))
    if ch == 1 : 
        st.create_file()
    elif ch == 2 : 
        st.update_file()
    elif ch == 3 : 
        print("\n\n")
        topic_name = input("Enter Topic Name : ".center(60))
        st.take_attendance(topic_name)
    else : 
        print("\n\nInvalid Choice Try Again ".center(60))
        

if __name__ == "__main__" : 
    os.system('cls')
    print("*"*60)
    print("*"*60)
    print("\n\n\n")
    main()
    print("*"*60)
    print("*"*60)
    print("\n\n\n")
    input("...........press any key to exit from progam..........")
    os.system('cls')
    
