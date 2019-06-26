import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("The server socket is created")
#host = socket.gethostbyname(socket.gethostname())
host = "192.168.0.147"
port = 1234
server_socket.bind((host,port))
print("The server socket is created at ip {} and port {}".format(host,port))
server_socket.listen()
print('The socket is ready to listen to client')
client_socket,client_addr = server_socket.accept()
#print(client_socket)
#print(client_addr)
print("The client is at ip {} and port {}".format(client_addr[0],client_addr[1]))
while True:
    smsg = input("Server : ")
    client_socket.send(smsg.encode())
    if smsg.strip().lower() == "bye":
        print("Connection is closed by server")
        client_socket.close()
        server_socket.close()
        break
    cmsg = client_socket.recv(1024)
    print("Client : ",cmsg.decode())
    if cmsg.decode().strip().lower() == "bye":
        print("COnnection is closed by client")
        client_socket.close()
        server_socket.close()
        break
