import requests

API_KEY = "d9824be61c57443180958c74c0c5f873"  
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}


def get_top_scorers(limit=10):
    url = f"{BASE_URL}/competitions/PD/scorers"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"API error: {resp.status_code} – {resp.text}")
        return

    data = resp.json()
    scorers = data.get("scorers", [])

    print(f"=== La Liga Top {limit} Goal Scorers ===")
    for i, player in enumerate(scorers[:limit], start=1):
        name = player["player"]["name"]
        team = player["team"]["name"]
        goals = player["goals"]
        penalties = player.get("penalties", 0)
        print(f"{i}. {name} ({team}) – {goals} goals ({penalties} pens)")


if __name__ == "__main__":
    get_top_scorers()
