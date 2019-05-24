# client side
import socket
client = socket.socket()
client.connect(("localhost",12345))
while True : 
    msg = client.recv(1024).decode()
    print("server--> ",msg)
    if msg.lower().strip() == 'bye' : 
        client.send('bye'.encode())
        client.close()
        break
    msg = input("client--> ")
    client.send(msg.encode())
