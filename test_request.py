import requests

url = "http://stokejo.com:5050/predict"
payload = {
    "Popularity": 60,
    "danceability": 0.85,
    "energy": 0.3,
    "speechiness": 0.04,
    "acousticness": 0.22,
    "instrumentalness": 0.5,
    "valence": 0.6,
    "duration_ms": 173968
}

response = requests.post(url, json=payload)
print(response.json())
