import requests

API_KEY = "d9824be61c57443180958c74c0c5f873"   
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}

def get_finished_matches():
    url = f"{BASE_URL}/competitions/PD/matches"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"API error: {resp.status_code} – {resp.text}")
        return

    data = resp.json()
    matches = data.get("matches", [])

    print("=== Finished La Liga Matches ===")
    found = False
    for match in matches:
        if match.get("status") == "FINISHED":   # only completed matches
            found = True
            home = match['homeTeam']['name']
            away = match['awayTeam']['name']
            score_home = match['score']['fullTime']['home']
            score_away = match['score']['fullTime']['away']
            utc_date = match['utcDate']  # ISO timestamp

            print("----------------------------------")
            print(f"{home} {score_home} - {score_away} {away}")
            print(f"Date: {utc_date}")

    if not found:
        print("No finished matches found yet.")

if __name__ == "__main__":
    get_finished_matches()
