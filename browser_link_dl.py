import requests

# URL for accessing the browser's DevTools protocol
url = "http://localhost:9222/json"

try:
    # Fetch the list of open tabs
    response = requests.get(url)
    tabs = response.json()

    # Open a file to store URLs, using UTF-8 encoding
    with open("brave_tabs.txt", "w", encoding="utf-8") as file:
        # Indented block starts here
        for tab in tabs:
            file.write(f"{tab['title']}: {tab['url']}\n")

    print("URLs have been saved to brave_tabs.txt")

except requests.exceptions.ConnectionError:
    print("Could not connect to Brave. Make sure Brave is running with remote debugging enabled.")
