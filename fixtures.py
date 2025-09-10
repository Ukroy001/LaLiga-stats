import requests
from datetime import datetime, timedelta

API_KEY = "d9824be61c57443180958c74c0c5f873"   
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY}


def get_upcoming_fixtures():
    # Get current matchday
    comp_url = f"{BASE_URL}/competitions/PD"
    comp_resp = requests.get(comp_url, headers=HEADERS)
    if comp_resp.status_code != 200:
        print(f"API error: {comp_resp.status_code} – {comp_resp.text}")
        return

    comp_data = comp_resp.json()
    current_matchday = comp_data.get("currentSeason", {}).get("currentMatchday")

    if not current_matchday:
        print("Could not determine current matchday.")
        return

    # Fetch matches for this matchday
    matches_url = f"{BASE_URL}/competitions/PD/matches?matchday={current_matchday}"
    resp = requests.get(matches_url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"API error: {resp.status_code} – {resp.text}")
        return

    data = resp.json()
    matches = data.get("matches", [])

    print(f"=== Upcoming Matches – La Liga Matchday {current_matchday} ===")
    found = False
    for match in matches:
        if match.get("status") != "FINISHED":  # only future or live matches
            found = True
            home = match['homeTeam']['name']
            away = match['awayTeam']['name']
            utc_date = match['utcDate']  # ISO format string
            status = match['status']

            # Convert UTC to IST (+5:30)
            match_time_utc = datetime.fromisoformat(utc_date.replace("Z", "+00:00"))
            match_time_ist = match_time_utc + timedelta(hours=5, minutes=30)
            local_time_str = match_time_ist.strftime("%Y-%m-%d %H:%M IST")

            print("----------------------------------")
            print(f"{home} vs {away}")
            print(f"Date & Time: {local_time_str} | Status: {status}")

    if not found:
        print("No upcoming matches in this matchday.")


if __name__ == "__main__":
    get_upcoming_fixtures()
