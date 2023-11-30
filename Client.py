import socket

def run_client():
    # create a socket object 
    print("[PROGRESS] Creating Socket...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[PROGRESS] Socket successfully created") 

    server_ip = "127.0.0.1"  # server's IP address
    server_port = 8000  # server's port number
    # establish connection with server

    print("[PROGRESS] Connecting Socket to port", server_port)  
    client.connect((server_ip, server_port)) 
    print("[PROGRESS] Socket connected successfully to port", server_port)

    while True:
        # input message and send it to the server
        msg = input("Enter message(TO EXIT, ENTER 'Close'): ")
        print("[PROGRESS] Sending and Encoding data...")
        client.send(msg.encode("utf-8")[:1024]) 
        print("[PROGRESS] Data sent successfully to Server") 

        # receive message from the server 
        print("[PROGRESS] Receiving Data from server")
        response = client.recv(1024) 
        print("[PROGRESS] Decoding received data...") 
        response = response.decode("utf-8")

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
        if response.lower() == "closed":
            break

        print(f"Data received: {response}")

    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

run_client() 