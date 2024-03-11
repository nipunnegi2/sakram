import socket

def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        return f"Error: {e}"

# Take user input for the domain
domain_name = input("Enter the domain name: ")

# Convert domain to IP address
ip_address = domain_to_ip(domain_name)

# Display the result
print(f"The IP address of {domain_name} is: {ip_address}")
