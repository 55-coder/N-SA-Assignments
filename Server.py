import socket 
import subprocess
import platform #Added for platform detection 

def run_server():
    # create a socket object 
    print("[PROGRESS] Creating Socket...") 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[PROGRESS] Socket successfully created")

    server_ip = "127.0.0.1"
    port = 8000

    # bind the socket to a specific address and port
    server.bind((server_ip, port))
    print(f"[PROGRESS] Socket is binded to Ip address {server_ip} and to port {port}") 

    #trace the route before listening for incoming connections
    trace_command = ""
    if platform.system() == "Linux":
        trace_command = "traceroute"
    elif platform.system() == "Windows":
        trace_command = "tracecert"
    else:
        print("Platform not supported for tracing the route.")

    if trace_command:
        trace_route_command = f"{trace_command} {server_ip}"
        print(f"[PROGRESS] Tracing route to {server_ip}...")
        subprocess.run(trace_route_command. shell = True)
    else:
        print("Route tracing not supported on this platform")
        
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}") 

    while True:
        # receive data from the client
        print("[PROGRESS] Receiving Data from Client...")  
        request = client_socket.recv(1024)
        print("[PROGRESS] Decoding received data...") 
        request = request.decode("utf-8") # convert bytes to string 
                
        # if we receive "close" from the client, then we break
        # out of the loop and close the conneciton
        if request.lower() == "close":
            # send response to the client which acknowledges that the
            # connection should be closed and break out of the loop
            client_socket.send("closed".encode("utf-8")) 
            break 

        print(f"Data received: {request}")

        response = "accepted".encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
        client_socket.send(response)

    # close connection socket with the client
    client_socket.close()
    print("Connection to client closed") 
    server.close() 
    
run_server()
