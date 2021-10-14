import socket,platform,os
SRV_ADDR = ""
SRV_PORT = 6666
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((SRV_ADDR,SRV_PORT))
s.listen()
connection,address = s.accpet()
while 1:
    try:
        data = connection.recV(1024)
    except:continue
    if(data.decode('utf-8') == '1'):
        tosend = platform.platform() + "" + platform.machine()
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '2'):
        data = connection.recV(1024)
        try:
            file list = os.listdir(data.decode('utf-8'))
            tosend = ""
            for x in file list:
                tosend += "," + x
        except:
            tosend = "wrongpath"
            connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '0'):
        connection.close()
        connection,address = s.accept()                        