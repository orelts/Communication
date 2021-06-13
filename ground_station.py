#!/usr/bin/env python
import socket


def command_input():
    inp = input("Enter cmd input please\n")
    if inp[:4] == "info":
        return inp
    else:
        return None


TCP_IP = '127.0.0.1'
TCP_PORT = 6800
MAX_TRIES = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)

while True:

    msg = command_input()
    if msg is None:
        continue

    # flushing the recv buffer before sending command and receiving usefull feedback
    conn.recv(4096)

    data_ok = False
    attempt = 0
    while attempt < MAX_TRIES:
        print("Sending msg try {} ".format(attempt))
        conn.send(msg.encode())
        data = conn.recv(4096)
        data_ok = True
        break
    if data_ok:
        print("received data: ", data)
    else:
        print(" didnt received msg\n")

conn.close()
