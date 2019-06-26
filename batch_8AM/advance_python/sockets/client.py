import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = socket.gethostbyname(socket.gethostname())
host = '192.168.0.174'
port = 1234
server_socket.connect((host,port))
print("Server is connected")
while True:
    smsg = server_socket.recv(1024)
    print("Server : ",smsg.decode())
    if smsg.decode().strip().lower() == "bye":
        print("Connection is closed by server")
        server_socket.close()
        break
    cmsg = input("Client : ")
    server_socket.send(cmsg.encode())
    if cmsg.strip().lower() == "bye":
        print("Connection is closed by client")
        server_socket.close()
        break
