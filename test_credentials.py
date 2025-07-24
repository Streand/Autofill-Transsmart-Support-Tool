import os
import json

def test_credentials():
    credentials_file = os.path.join(os.path.dirname(__file__), "credentials.json")
    print(f"Looking for credentials file at: {credentials_file}")
    print(f"File exists: {os.path.exists(credentials_file)}")
    
    if os.path.exists(credentials_file):
        try:
            with open(credentials_file, 'r') as f:
                creds = json.load(f)
                username = creds.get("username")
                password = creds.get("password")
                print(f"Username loaded: {username}")
                print(f"Password loaded: {'*' * len(password) if password else 'None'}")
                return username, password
        except Exception as e:
            print(f"Error reading credentials: {e}")
    return None, None

if __name__ == "__main__":
    test_credentials()