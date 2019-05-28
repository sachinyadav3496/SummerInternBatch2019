user1 = { 
      'name' : 'ram',
      'bal' : 5000,
      'password' : 'redhat',
      }

user2 = { 
      'name' : 'shyam',
      'bal' : 45000,
      'password' : 'asimov',
      }

user3 = { 
      'name' : 'hari',
      'bal' : 50000,
      'password' : 'hatbe',
      }

import shelve

db  = shelve.open("database/bank.db",writeback=True)

db['1001'] = user1
db['1002'] = user2
db['1003'] = user3

db['last_acc'] = 1003

db.close()

print("Data Exported Sucessfully")
