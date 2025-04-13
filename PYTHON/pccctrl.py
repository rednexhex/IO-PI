
from gpiozero import Button
from gpiozero import OutputDevice
from signal import pause
import socket
import threading
import time

iodata = "unknown "

sensepin1 = 2
sensepin2 = 3
sensepin3 = 4
sensepin4 = 17
sensepin5 = 27
sensepin6 = 22
sensepin7 = 19
sensepin8 = 21
sense1 = Button(sensepin1, pull_up=True)
sense2 = Button(sensepin2, pull_up=True)
sense3 = Button(sensepin3, pull_up=True)
sense4 = Button(sensepin4, pull_up=True)
sense5 = Button(sensepin5, pull_up=True)
sense6 = Button(sensepin6, pull_up=True)
sense7 = Button(sensepin7, pull_up=True)
sense8 = Button(sensepin8, pull_up=True)


relaypin1 = 14
relaypin2 = 15
relaypin3 = 18
relaypin4 = 23
relaypin5 = 24
relaypin6 = 25
relaypin7 = 8
relaypin8 = 7
relay1 = OutputDevice(relaypin1, active_high=True, initial_value=False) 
relay2 = OutputDevice(relaypin2, active_high=True, initial_value=False)
relay3 = OutputDevice(relaypin3, active_high=True, initial_value=False) 
relay4 = OutputDevice(relaypin4, active_high=True, initial_value=False)
relay5 = OutputDevice(relaypin5, active_high=True, initial_value=False) 
relay6 = OutputDevice(relaypin6, active_high=True, initial_value=False)
relay7 = OutputDevice(relaypin7, active_high=True, initial_value=False) 
relay8 = OutputDevice(relaypin8, active_high=True, initial_value=False)


HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 1081       # Port to bind the server

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address after disconnect
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server listening on {HOST}:{PORT}")

        while True:  # Keep the server running indefinitely
            conn, addr = server_socket.accept()
            with conn:
                welcomemsg = "Welcome to MattyPi\r\n\n"
                tagmsg = "Any sufficiently advanced technology is indistinguishable from magic\r\n\n"
                conn.sendall(welcomemsg.encode())
                conn.sendall(tagmsg.encode())
                
                
                def pin1_closed():
                 current_state = "iostate,1:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin1_opened():
                 current_state = "iostate,1:0\r\n" 
                 conn.sendall(current_state.encode())                 
                 
                
                def pin2_closed():
                 current_state = "iostate,2:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin2_opened():
                 current_state = "iostate,2:0\r\n" 
                 conn.sendall(current_state.encode()) 
                 
                 
                def pin3_closed():
                 current_state = "iostate,3:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin3_opened():
                 current_state = "iostate,3:0\r\n" 
                 conn.sendall(current_state.encode()) 
                 
                 
                def pin4_closed():
                 current_state = "iostate,4:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin4_opened():
                 current_state = "iostate,4:0\r\n" 
                 conn.sendall(current_state.encode())
                 
                def pin5_closed():
                 current_state = "iostate,5:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin5_opened():
                 current_state = "iostate,5:0\r\n" 
                 conn.sendall(current_state.encode())                 
                 
                
                def pin6_closed():
                 current_state = "iostate,6:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin6_opened():
                 current_state = "iostate,6:0\r\n" 
                 conn.sendall(current_state.encode()) 
                 
                 
                def pin7_closed():
                 current_state = "iostate,7:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin7_opened():
                 current_state = "iostate,7:0\r\n" 
                 conn.sendall(current_state.encode()) 
                 
                 
                def pin8_closed():
                 current_state = "iostate,8:1\r\n" 
                 conn.sendall(current_state.encode())
                                
                def pin8_opened():
                 current_state = "iostate,8:0\r\n" 
                 conn.sendall(current_state.encode())  

                sense1.when_pressed = pin1_closed
                sense1.when_released = pin1_opened
                sense2.when_pressed = pin2_closed
                sense2.when_released = pin2_opened         
                sense3.when_pressed = pin3_closed
                sense3.when_released = pin3_opened
                sense4.when_pressed = pin4_closed
                sense4.when_released = pin4_opened 
                
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break  # Client disconnected
                    global iodata 
                    iodata = data.decode()
                    print(f"Received: {data.decode()}")
                    print(f"iodata : {iodata}")
                                
                
def monitor_iodata():
    global iodata
    last_value = iodata
    
    while True:
        if iodata.strip() != last_value.strip():  # Detect changes
            #word1 = iodata.split(",")
            #word2 = iodata.split(":")
            #print(f"word1 = {word1}")
            #print(f"word2 = {word2}")
            

            if iodata.strip() == "relstate,1:1":
                relay1.on()
            
            if iodata.strip() == "relstate,1:0":
                relay1.off()
            
            if iodata.strip() == "relstate,1:2":
                relay1.on()
                time.sleep(3)
                relay1.off()               
                            
                
            if iodata.strip() == "relstate,2:1":
                relay2.on()
            
            if iodata.strip() == "relstate,2:0":
                relay2.off()
                
            if iodata.strip() == "relstate,2:2":
                relay2.on()
                time.sleep(3)
                relay2.off()                
                          
                
            if iodata.strip() == "relstate,3:1":
                relay3.on()
            
            if iodata.strip() == "relstate,3:0":
                relay3.off()
                
            if iodata.strip() == "relstate,3:2":
                relay3.on()
                time.sleep(3)
                relay3.off()                         
                            
                
            if iodata.strip() == "relstate,4:1":
               relay4.on()
            
            if iodata.strip() == "relstate,4:0":
                relay4.off()
                
            if iodata.strip() == "relstate,4:2":
                relay4.on()
                time.sleep(3)
                relay4.off()                         
            
                
            if iodata.strip() == "relstate,5:1":
                relay5.on()
            
            if iodata.strip() == "relstate,5:0":
                relay5.off()
                
            if iodata.strip() == "relstate,5:2":
                relay5.on()
                time.sleep(3)
                relay5.off()                         
                            
                
            if iodata.strip() == "relstate,6:1":
                relay6.on()
            
            if iodata.strip() == "relstate,6:0":
                relay6.off()
                
            if iodata.strip() == "relstate,6:2":
                relay6.on()
                time.sleep(3)
                relay6.off()                         
                          
                
            if iodata.strip() == "relstate,7:1":
                relay7.on()
            
            if iodata.strip() == "relstate,7:0":
                relay7.off()
                
            if iodata.strip() == "relstate,7:2":
                relay7.on()
                time.sleep(3)
                relay7.off()                         
                            
                
            if iodata.strip() == "relstate,8:1":
               relay8.on()
            
            if iodata.strip() == "relstate,8:0":
                relay8.off()
                
            if iodata.strip() == "relstate,8:2":
                relay8.on()
                time.sleep(3)
                relay8.off()
                
              
            if iodata.strip() == "relstate,0:1":
                relay1.on() 
                relay2.on()
                relay3.on() 
                relay4.on()
                relay5.on()
                relay6.on()
                relay7.on()
                relay8.on()            
                
            if iodata.strip() == "relstate,0:0":
                relay1.off() 
                relay2.off()
                relay3.off() 
                relay4.off()
                relay5.off()
                relay6.off()
                relay7.off()
                relay8.off()                                               
                
            
            last_value = iodata  # Update the last known value

        time.sleep(0.1)  # Small delay to reduce CPU usage         
        

if __name__ == "__main__":
 # start_server()
 server_thread = threading.Thread(target=start_server, daemon=True)
 server_thread.start()  # Start the server in a separate thread   
 
 monitor_thread = threading.Thread(target=monitor_iodata, daemon=True)
 monitor_thread.start()  # Start monitoring iodata
 
 pause()	