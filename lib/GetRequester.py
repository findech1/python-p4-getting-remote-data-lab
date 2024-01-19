import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error making GET request: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()

        if response_body is not None:
            try:
                json_data = json.loads(response_body)
                return json_data
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
                return None

# Example usage:
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
get_requester = GetRequester(url)

# Get response body
response_body = get_requester.get_response_body()

if response_body is not None:
    print(f"Response Body:")
    print(response_body)

# Load JSON data
json_data = get_requester.load_json()

if json_data is not None:
    print("JSON Data:")
    print(json_data)
