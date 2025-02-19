
from gpiozero import Button
from gpiozero import OutputDevice
from signal import pause
import socket
import threading
import time

iodata = "unknown "

sensepin1 = 5
sensepin2 = 6
sensepin3 = 13
sensepin4 = 19
sense1 = Button(sensepin1, pull_up=True)
sense2 = Button(sensepin2, pull_up=True)
sense3 = Button(sensepin3, pull_up=True)
sense4 = Button(sensepin4, pull_up=True)


relaypin1 = 14
relaypin2 = 15
relaypin3 = 23
relaypin4 = 24
relay1 = OutputDevice(relaypin1, active_high=False, initial_value=False) 
relay2 = OutputDevice(relaypin2, active_high=False, initial_value=False)
relay3 = OutputDevice(relaypin3, active_high=False, initial_value=False) 
relay4 = OutputDevice(relaypin4, active_high=False, initial_value=False)

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 48971       # Port to bind the server

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
                 current_state = "io1closed\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin1 closed (circuit completed)")
                
                def pin1_opened():
                 current_state = "io1open\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin1 opened (circuit broken)")
                 
                 
                
                def pin2_closed():
                 current_state = "io2closed\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin2 closed (circuit completed)")
                
                def pin2_opened():
                 current_state = "io2open\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin2 opened (circuit broken)")
                 
                 
                def pin3_closed():
                 current_state = "io3closed\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin3 closed (circuit completed)")
                
                def pin3_opened():
                 current_state = "io3open\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin3 opened (circuit broken)")
                 
                 
                def pin4_closed():
                 current_state = "io4closed\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin4 closed (circuit completed)")
                
                def pin4_opened():
                 current_state = "io4open\r\n" 
                 conn.sendall(current_state.encode())
                 print("Pin4 opened (circuit broken)")

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
    last_value = iodata  # Store the initial value of iodata

    while True:
        if iodata.strip() != last_value.strip():  # Detect changes
            # print(f"iodata changed to: {iodata.strip()}")

            # Take action based on the new iodata value
            if iodata.strip() == "rel2-on":
                relay1.on()
                # print("Relay 1 turned ON")

            if iodata.strip() == "rel2-off":
                relay1.off()
                # print("Relay 1 turned OFF")
                
                
            if iodata.strip() == "rel2-on":
                relay2.on()
                # print("Relay 1 turned ON")

            if iodata.strip() == "rel2-off":
                relay2.off()    
                
                
            if iodata.strip() == "rel3-on":
                relay3.on()
                # print("Relay 1 turned ON")

            if iodata.strip() == "rel3-off":
                relay3.off()
                
                
            if iodata.strip() == "rel4-on":
                relay4.on()
                # print("Relay 1 turned ON")

            if iodata.strip() == "rel4-off":
                relay4.off()                                        

            last_value = iodata  # Update the last known value

        time.sleep(0.1)  # Small delay to reduce CPU usage         
        

if __name__ == "__main__":
 # start_server()
 server_thread = threading.Thread(target=start_server, daemon=True)
 server_thread.start()  # Start the server in a separate thread   
 
 monitor_thread = threading.Thread(target=monitor_iodata, daemon=True)
 monitor_thread.start()  # Start monitoring iodata
 
 pause()	