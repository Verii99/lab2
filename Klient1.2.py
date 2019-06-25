import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
N = input("Введите N = ")
M = input("Введите M = ")
sock.send(N.encode('utf-8'))
sock.send(M.encode('utf-8'))
print("Введите матрицу: ")
while True:
    data = sock.recv(2048)
    print(data.decode('utf-8'))
sock.close()
