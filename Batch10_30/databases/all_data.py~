import MySQLdb as sql 



try : 

    db = sql.connect(host="192.168.56.129",port=3306,user="sachin",password="redhat",
        database="grras")

    cur = db.cursor()
except Exception as e : 
    print("!!Error!! something went wrong",e)
    print("Check DATA Base Connection ")

    exit(0)


command = "select * from student;"
cur.execute(command)

data = cur.fetchall()

# ( (id,name,course,fees),(),())

print("id\tname\tcourse\tfees")
for each_tuple in data : 
    print(*each_tuple,sep='\t')

cur.close()
db.close()
