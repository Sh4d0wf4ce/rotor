import socket

def server():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    print ("Socket successfully created")
    server_socket.bind((host,port))
    print ("socket binded to %s" %(port))

    server_socket.listen(1)
    print ("socket is listening")

    
    while True:
        conn, adress = server_socket.accept()
        print("Connection from: "+ str(adress))
        data = conn.recv(1024).decode()
        print(data)
        message = "Rotating the rotor to the "+data
        conn.send(message.encode())

    conn.close()

if __name__ == '__main__':
    server()
