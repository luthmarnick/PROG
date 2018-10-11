import requests

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("https://webservices.ns.nl/ns-api-avt?station=ut", auth=('luthmarnick@hotmail.com', 'xxX8_vL4EWukcoy3OQOrET9M9vDP3lHIdEj8Y1KOapRzitKuKnVw0A'))

# Print the status code of the response.
print(response.status_code)