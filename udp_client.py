#!/usr/bin/env python3
import socket
import sys
import msvcrt as m
def wait():
    m.getch()

# The client code that requests a spot in the queue, a
# nd notifies the server when the student is finished getting help during office hours.

# Get command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]

# The client, when run, must notify the server that a new student wants to join the office hours queue.
# The client must then wait for the server to notify it that it is now at the head of the queue.
# The client then must notify the server when the student is finished by waiting for any input on stdin and then
# sending a packet to the server. At that point the client can safely exit.


# Create a socket and notify the server we want to be added to the office
# hour queue.

servername = 'localhost'
BUFFERSIZE = 1024

s = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)

#s.connect((servername,port))
#s.bind((host, port))
s.sendto(name.encode(), (host,port))

# do while loop maybe so it executes at least once
while True:
    (message, address) = s.recvfrom(BUFFERSIZE)
    message = message.decode()
    print("Message:", message, "Address:", address)
    print("Name:", name)
    if (message == name):
        print("waiting for input")
        x = input()
        if(len(x) > 0):
            print("Sending remove response to server")
            s.sendto(x.encode(), (host,port))
            break


s.close()

# # s.sendto(message, host,port)


# # (host, port)

# # print(host)

# # Wait for head of queue message from the server.



# # Wait for user to signal that we are done (via stdin) and notify the server.
