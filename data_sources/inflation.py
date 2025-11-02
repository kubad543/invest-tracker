import requests

API_KEY = ""
url = "https://bdl.stat.gov.pl/api/v1/subjects?format=json"
headers = {"X-ClientId": API_KEY, "User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print(response.status_code, response.text)
