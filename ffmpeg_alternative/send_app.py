import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.10", 8888))  # Doesn't work if socket is closed before sock.recv
# sock.connect(("127.0.0.10", 8002))  # Works fine

sock.send(
    b"PUT /test.m3u8 HTTP/1.1\r\n"
    b"Host: uwsgi\r\n"
    b"X-Server-Name: wusgi\r\n"
    b"Connection: close\r\n"
    b"Transfer-Encoding: chunked\r\n"
    b"\r\n"
)

chunk_size = 100

for _ in range(5):
    sock.send("{:x}\r\n".format(chunk_size).encode() +
              bytes(chunk_size) +
              b"\r\n")

sock.send(b"0\r\n\r\n")

# Comment those 2 lines to reproduce the problem
# response = sock.recv(4096)
# print(response.decode())

sock.close()