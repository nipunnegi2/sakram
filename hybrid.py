import whois
import socket
import dns.resolver
import requests

def get_domain_info(domain_name):
    # Get basic domain information using whois
    domain_info = whois.whois(domain_name)

    # IP address
    try:
        ip_address = socket.gethostbyname(domain_name)
        domain_info['ip_address'] = ip_address
    except socket.gaierror as e:
        print(f"Error: {e}")
        domain_info['ip_address'] = None

    # DNS information
    try:
        dns_records = dns.resolver.resolve(domain_name, 'A')
        domain_info['dns_records'] = [record.address for record in dns_records]
    except dns.resolver.NXDOMAIN:
        print(f"DNS Error: Domain not found.")
        domain_info['dns_records'] = None
    except dns.resolver.NoAnswer:
        print(f"DNS Error: No A records found.")
        domain_info['dns_records'] = None

    return domain_info

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
            print("\nDomain Information:")
            print(f"Name: {domain}")
            print(f"Whois Information: {get_domain_info(domain)}")

            print("\nLocation Information:")
            print(f"IP Address: {data.get('ip')}")
            print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
            print(f"ISP: {data.get('org')}")

    except (socket.gaierror, requests.exceptions.RequestException) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")
    api_key = 'c0ec2816fd3065'
    get_location_info(api_key, domain_name)
