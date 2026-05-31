import requests

# API URL
url = "https://catfact.ninja/fact"

try:
    # Fetch data from API
    response = requests.get(url)

    # Convert JSON response into Python dictionary
    data = response.json()

    # Display formatted output
    print("===== API & JSON Task =====")
    print("API Used: Cat Facts API")
    print("Status Code:", response.status_code)
    print("\nRandom Cat Fact:")
    print(data["fact"])
    print("\nFact Length:", data["length"])

except Exception as e:
    print("Error occurred:", e)