import socket

def get_ip_address():
    try:
        # Create a socket object to get local machine name
        host_name = socket.gethostname()

        # Get the IP address of the local machine
        ip_address = socket.gethostbyname(host_name)

        print(f"Your IP Address is: {ip_address}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ip_address()