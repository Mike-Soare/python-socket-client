#!/usr/bin/python

import socket, getopt, sys

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:p:l:",["host=","port=","log="])
    except getopt.GetoptError:
        print("client.py -s <HOST_IP> -p <HOST_PORT> -l <LOG_FILE>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('client.py -s <HOST_IP> -p <HOST_PORT> -l <LOG_FILE>')
            sys.exit()
        elif opt in ("-s", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-l", "--log"):
            log = arg

    print("\nHOST=", host)
    print("PORT=", port)
    print("LOG=",log)

    s = socket.socket(type=socket.SOCK_STREAM)

    try:
        s.connect((host,int(port)))
    except:
        sys.exit("\nFailed to established connection...\n\nPlease rerun the program and insert a valid IP Address and Port.")
    else:
        print("\nConnection to ", host, " with port ", port, " was successfully connected.\n")

    msg = input('Enter the message you would like to send: ')
    
    s.send(msg.encode())
    received = s.recv(1024).decode("utf-8")
    
    print("Reply from ", host, " : ", received)
    
    f = open(log, "a")
    f.write(received)

    f.close()
    s.close()
    
    exit

main(sys.argv[1:])
