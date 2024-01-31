import requests

def get_public_ip_address():
    try:
        # Use an external service to get your public IP address
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()

        public_ip = data["ip"]
        print(f"Your Public IP Address is: {public_ip}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_public_ip_address()