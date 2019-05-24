import socket
server = socket.socket()
server.bind(("localhost",12345))
server.listen()
client,address = server.accept()
while True : 
    msg = input("server --> ").encode()
    client.send(msg)
    msg = client.recv(1024).decode()
    print("client -->",msg)
    if 'bye' == msg.lower().strip() : 
        client.close()
        server.close()
        break
