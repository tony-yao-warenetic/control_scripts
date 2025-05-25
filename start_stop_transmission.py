import requests

SERVER_URL_RIGHT = "https://no-more-waiting-4-lunch-atest20061206.replit.app/send_diagnostic/Start"

response = requests.post(SERVER_URL_RIGHT)
response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
    