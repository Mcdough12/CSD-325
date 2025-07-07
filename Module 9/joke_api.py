# joke_api.py
import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

# Test connection
print("Connection status:", response.status_code)

# Raw response
print("\nRaw JSON response:\n", response.text)

# Formatted output
if response.status_code == 200:
    joke = response.json()
    print("\nFormatted Joke:")
    print(f"{joke['setup']} — {joke['punchline']}")
else:
    print("Failed to retrieve joke.")
