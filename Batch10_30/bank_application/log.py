import time

def update_log(log_type,message) : 

    s = f"\n{time.ctime()}:{log_type}:{message}"
    fp = open("log.txt","a")
    fp.write(s)
    fp.close()
