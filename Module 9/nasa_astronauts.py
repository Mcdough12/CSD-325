# nasa_astronauts.py
import requests

# Get the data from the NASA astronaut API
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

# Print raw response
print("Raw JSON response:\n", response.text)

# Print formatted response
print("\nFormatted Output:")
if response.status_code == 200:
    data = response.json()
    print(f"There are currently {data['number']} people in space:\n")
    for person in data['people']:
        print(f"Name: {person['name']}, Craft: {person['craft']}")
else:
    print("Failed to retrieve data.")
