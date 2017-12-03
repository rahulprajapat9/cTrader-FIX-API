import socket, time
from datetime import datetime

def ConstructHeader(SenderCompID, TargetCompID, SenderSubID, TargetSubID, messageSequenceNumber):
    header = ''

    # Version of FIX
    header += "8=FIX.4.4|"

    message = ''

    # Type of message, A = String
    message += "35=A|"

    message += "49="  + SenderCompID +  "|"
    message += "56="  + TargetCompID +  "|"

    message += "50="  + SenderSubID +  "|"
    message += "57="  + TargetSubID +  "|"

    message += "34="  + messageSequenceNumber +  "|"
    message += "52="  + str(datetime.today()) +  "|"

    return header, message

def ConstructTrailer(headerAndBody):
    headerAndBody = str(headerAndBody.replace('|', '\u0001'))
    chksum = str(reduce(lambda x,y:x+y, map(ord, headerAndBody)) % 256)
    chksum = chksum.zfill(3)

    return chksum
    # expected 131

def LogonMessage(heartBeatSeconds, username, password, resetSeqNum):
    body = ''

    # Encryption
    body += "98=0|"

    body += "108="  + heartBeatSeconds +  "|"

    if resetSeqNum:
        body += "141=Y|"


    body += "553=" + username + "|"
    body += "554=" + password + "|"

    return body

def LogonPacket():

    # Header
    SenderCompID = 'pepperstone.3224363'
    TargetCompID = 'CSERVER'

    #SenderSubID = 'QUOTE'
    SenderSubID = 'any_string'
    TargetSubID = 'QUOTE'
    messageSequenceNumber = '1'

    header, message = ConstructHeader(SenderCompID, TargetCompID, SenderSubID, TargetSubID, messageSequenceNumber)
    print 'Header construction completed'
    print 'Header is: ', header, '\n'

    # Body
    heartBeatSeconds = '30'
    username = '3224363'
    password = '3689'
    resetSeqNum = 1

    body = LogonMessage(heartBeatSeconds, username, password, resetSeqNum)
    print 'Body construction completed'
    print 'Body message is: ', body, '\n'

    length = len(message) + len(body)
    headerAndBody = header + message + body
    print 'Length of Messasge + Body is: ', length, '\n'
    headerAndBody += "9=" + str(length) + "|"

    #headerAndBody = '8=FIX.4.4|9=126|35=A|49=theBroker.12345|56=CSERVER|34=1|52=20170117-08:03:04|57=TRADE|50=any_string|98=0|108=30|141=Y|553=12345|554=passw0rd!|'

    # Trailer
    chksum = ConstructTrailer(headerAndBody)
    trailer = "10="+str(chksum)+"|"

    print 'Trailer construction completed'
    print 'Trailer is: ', trailer, '\n'

    headerAndBodyAndTrailer = headerAndBody + trailer
    print 'ctrader packet is: ', headerAndBodyAndTrailer, '\n'

    # ctrader packet constructor finished

    return headerAndBodyAndTrailer

def Main():
    host = 'h58.p.ctrader.com'
    port = 5201

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print 'Connection to Ctrader API successful\n'

    # Constructing ctrader packet
    headerAndBodyAndTrailer = LogonPacket()

    # Debug
    #headerAndBodyAndTrailer = '8=FIX.4.4|9=126|35=A|49=theBroker.12345|56=CSERVER|34=1|52=20170117-08:03:04|57=TRADE|50=any_string|98=0|108=30|141=Y|553=12345|554=passw0rd!|10=131|'
    #print headerAndBodyAndTrailer

    while headerAndBodyAndTrailer!='q':
        s.send(headerAndBodyAndTrailer)
        print 'packet sent to ctrader!!!'
        print 'waiting to receive response from ctrader...'
        data = s.recv(1024)
        print 'Received from ctrader: ', str(data)

    s.close()


if __name__ == '__main__':
    Main()



