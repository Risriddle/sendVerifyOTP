import requests
import base64
import configparser


# Load configuration file
config = configparser.ConfigParser()
config.read('config.ini')


def send(no):
    url=config['DEFAULT2']['URL']
    auth_token=config['DEFAULT2']['AUTH_TOKEN']
    headers = {
        "Content-Type": "application/json",
        "Accept-Language": "en-US"
    }
    data = {
        "identity": {
            "type": "number",
            "endpoint": no,
            "message": "make lode"
        },
        "method": "sms"
    }

    # Encode the authentication token in base64
    auth_token_bytes = auth_token.encode('utf-8')
    encoded_auth_token = base64.b64encode(auth_token_bytes).decode('utf-8')
    auth_header = f"Basic {encoded_auth_token}"

    headers['Authorization'] = auth_header

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("SMS verification request sent successfully.")
        
    else:
        print(f"Failed to send SMS verification request. Status code: {response.status_code}")
        print(response.text)


def verify(no,otp):
    
    urll = config.get('DEFAULT3', 'URL')
    # Replace {no} with the actual value in the URL
    url = urll.replace('{no}', no)
    auth_token=config['DEFAULT3']['AUTH_TOKEN']
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "method": "sms",
        "sms": {
            "code": otp
        }
    }

    # Encode the authentication token in base64
    auth_token_bytes = auth_token.encode('utf-8')
    encoded_auth_token = base64.b64encode(auth_token_bytes).decode('utf-8')
    auth_header = f"Basic {encoded_auth_token}"

    headers['Authorization'] = auth_header

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Phone number {no} Verified")
        
    else:
        print(f"Failed to verify phone number. Status code: {response.status_code}")
       

