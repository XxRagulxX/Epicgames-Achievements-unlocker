import requests


deployment_id = ""  # Deployment ID of the product

url = f"https://api.epicgames.dev/epic/achievements/v1/public/achievements/product/{deployment_id}/locale/en?includeAchievements=true"

headers = {
    "Host": "api.epicgames.dev",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://overlay-override-service.cbce.live.on.epicgames.com",
    "Authorization": "Bearer ", # Add your access token here
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Referer": "https://overlay-override-service.cbce.live.on.epicgames.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send GET request
response = requests.get(url, headers=headers)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
