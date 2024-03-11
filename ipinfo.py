import requests

def get_location_info(api_key, domain):
    base_url = "http://ipinfo.io/"
    url = f"{base_url}{domain}/json?token={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print(f"Error: {data['error']['message']}")
        else:
            print("Location Information:")
            print(f"IP Address: {data.get('ip')}")
            print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
            print(f"ISP: {data.get('org')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


api_key = 'c0ec2816fd3065'
domain = input("Enter the IP address: ")

get_location_info(api_key, domain)
