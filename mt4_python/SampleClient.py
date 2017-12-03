#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq, time

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.0.115:5555")

#  Do 10 requests, waiting each time for a response
for request in range(1,11):
    socket.send(b"Hello")
    print 'msg sent, recv waiting ...'
    message = socket.recv()
    print("Received reply %s [%s]" % (request, message))
    time.sleep(10)