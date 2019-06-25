import socket
sock = socket.socket()
sock.bind(('', 9090))
while True:
    sock.listen(10)
    conn, addr = sock.accept()
    data = conn.recv(2048)
    if not data:
        break
    N = data.decode('utf-8')
    M = data.decode('utf-8')
    matrix = []
    for i in range(N):
        matrix.append([])
        for j in range(M):
            matrix[i].append(int(input()))
        print(matrix)

# сумма
    s = [0] * M
    for j in range(M):
        for i in range(N):
            s[j] += matrix[i][j]
    conn.send(s[j].encode('utf-8'))
# произведение
    p = [1] * M
    for j in range(M):
        for i in range(N):
            p[j] *= matrix[i][j]
    conn.send(p[j].encode('utf-8'))

# максимальное
    maxi = [0] * M
    for j in range(M):
        for i in range(N):
            if maxi[j] < matrix[i][j]:
              maxi[j] = matrix[i][j]
    conn.send(maxi[j].encode('utf-8'))
# минимальное
    mini = maxi
    for j in range(M):
        for i in range(N):
            if mini[j] > matrix[i][j]:
              mini[j] = matrix[i][j]
    conn.send(mini[j].encode('utf-8'))

conn.close()