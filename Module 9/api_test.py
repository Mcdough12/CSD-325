# api_test.py
import requests

response = requests.get('http://www.google.com')
print("Google connection status:", response.status_code)
