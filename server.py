import socket

def is_correct_username(data):
    if data == "username":
        return True
    return False

def is_correct_password(data):
    if data == "password":
        return True
    return False

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 55555)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(*client_address))

    # Send a welcome message to the client
    message = 'Enter your username!'
    client_socket.sendall(message.encode())

    # Receive and validate username from the client
    username_data = client_socket.recv(1024).decode()
    if is_correct_username(username_data):
        message = 'Enter your password!'
        client_socket.sendall(message.encode())

        # Receive and validate password from the client
        password_data = client_socket.recv(1024).decode()
        if is_correct_password(password_data):
            success_message = 'Authentication successful!'
            client_socket.sendall(success_message.encode())
        else:
            failure_message = 'Authentication failed. Incorrect password.'
            client_socket.sendall(failure_message.encode())
    else:
        failure_message = 'Authentication failed. Incorrect username.'
        client_socket.sendall(failure_message.encode())

    # Close the connection
    client_socket.close()
