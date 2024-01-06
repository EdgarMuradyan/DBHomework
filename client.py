import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 55555)
client_socket.connect(server_address)
print('Connected to {}:{}'.format(*server_address))

try:
    # Receive and print the welcome message from the server
    welcome_message = client_socket.recv(1024)
    print('Server says: {!r}'.format(welcome_message.decode()))

    # Prompt the user to enter a username
    username = input('Enter your username: ')
    client_socket.sendall(username.encode())

    # Receive and print the authentication message from the server
    auth_message = client_socket.recv(1024)
    print('Server says: {!r}'.format(auth_message.decode()))

    # Prompt the user to enter a password
    password = input('Enter your password: ')
    client_socket.sendall(password.encode())

    # Receive and print the authentication result from the server
    auth_result = client_socket.recv(1024)
    print('Server says: {!r}'.format(auth_result.decode()))

except Exception as e:
    print('Error:', e)

finally:
    # Close the connection
    client_socket.close()
