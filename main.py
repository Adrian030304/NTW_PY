import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',5500))
s.listen()

while True:
    client, address = s.accept() #accepts the connection
    print("Connected to: {}".format(address))
    client.send("You are connected!".encode())
    client.close()