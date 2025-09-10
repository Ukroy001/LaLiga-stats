import requests

API_KEY = "d9824be61c57443180958c74c0c5f873"   
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

def get_standings():
    url = f"{BASE_URL}/competitions/PD/standings"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"API error: {resp.status_code} – {resp.text}")
        return

    data = resp.json()
    standings_list = data.get("standings", [])

    # Find the TOTAL standings (overall table)
    total = next((s for s in standings_list if s.get("type") == "TOTAL"), None)
    if not total or not total.get("table"):
        print("No standings data available.")
        return

    print("=== La Liga Standings ===")
    for row in total["table"]:
        pos = row.get("position")
        name = row.get("team", {}).get("name")
        played = row.get("playedGames")
        won = row.get("won")
        draw = row.get("draw")
        lost = row.get("lost")
        points = row.get("points")
        gd = row.get("goalDifference")

        print(f"{pos}. {name} – {points} pts | {won}W {draw}D {lost}L | GD: {gd}")

if __name__ == "__main__":
    get_standings()
