
import socket
from signal import pause

# Server's address and port
SERVER_IP = '192.168.232.51'  # Replace with the server's IP address
SERVER_PORT = 1081       # Replace with the server's port number

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to {SERVER_IP}:{SERVER_PORT}")

    # Send data to the server
    message = "Hello, server!"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent: {message}")

    # Receive response from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

except ConnectionRefusedError:
    print("Connection refused. Make sure the server is running.")
except Exception as e:
    print(f"An error occurred: {e}")
#finally:
    # Close the connection
    #client_socket.close()
    #print("Connection closed.")
    
pause()    