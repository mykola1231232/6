import requests
import json

url = "https://api.jikan.moe/v4/top/anime"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    popular_anime = [
        {"title": anime["title"], "score": anime["score"]}
        for anime in data["data"]
    ]
    with open("popular_anime.json", "w", encoding="utf-8") as f:
        json.dump(popular_anime, f, ensure_ascii=False, indent=2)
else:
    print("Failed to fetch data from Jikan API")
