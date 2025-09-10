# ⚽ La Liga Stats Fetcher

A Python project to fetch and display **La Liga statistics** using the [Football-Data.org API](https://api.football-data.org/v4).  
The project is structured into separate modules for a **clean and organized codebase**, covering:

- ✅ All matches  
- 📅 Weekly matches  
- 🔮 Upcoming fixtures  
- 🎯 Goals & scoring details  
- 📊 League tables  

---

## 🚀 Features
- Fetch **all La Liga matches** from the API  
- Get **weekly match data** for analysis  
- Show **upcoming fixtures** with details  
- Track **goals and top scorers**  
- Display the **league standings table**  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **API:** [Football-Data.org](https://api.football-data.org/v4)  
- **Libraries:** `requests`, `json`  

---

## 📂 Project Structure
 ```
  a_liga_stats/
  │── all_matches.py # Fetch all La Liga matches
  │── weekly_matches.py # Get matches week by week
  │── upcoming_fixtures.py # Fetch upcoming fixtures
  │── goals.py # Retrieve goals and scorers
  │── tables.py # Display league standings
  │── main.py # Run and test all modules together


---

## 🔑 API Key
This project requires an **API key** from [Football-Data.org](https://api.football-data.org/v4).  
- Sign up on the website and get your key.  
- Replace `"YOUR_API_KEY_HERE"` inside the scripts where required.  

---

## ▶️ Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Ukroy001/la-liga-stats.git
   cd la-liga-stats
2. Install dependecies:
   pip install requests
3. Run the module:
python all_matches.py
python weekly_matches.py
python upcoming_fixtures.py
python goals.py
python tables.py

