import socket
import requests

def get_location_info(api_key, domain):
    try:
        # Convert domain to IP address using DNS lookup
        ip_address = socket.gethostbyname(domain)

        # Get location information using the IP address
        base_url = "http://ipinfo.io/"
        url = f"{base_url}{ip_address}/json?token={api_key}"

        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print(f"Error: {data['error']['message']}")
        else:
            print("Location Information:")
            print(f"IP Address: {data.get('ip')}")
            print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
            print(f"ISP: {data.get('org')}")

    except (socket.gaierror, requests.exceptions.RequestException) as e:
        print(f"Error: {e}")


api_key = 'c0ec2816fd3065'
domain = input("Enter the domain: ")

get_location_info(api_key, domain)
