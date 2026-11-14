# CampusFind – College Navigation System (VIT Bibwewadi, Pune)

A searchable campus map with shortest-path directions between places.
The map is a self-contained HTML/CSS/JavaScript page (`campusfind.html`),
served through a small Streamlit wrapper (`app.py`) so it can be hosted on
Streamlit Community Cloud.

## Files
- `app.py` – Streamlit entry point (embeds the page)
- `campusfind.html` – the whole app: map, search, directions
- `requirements.txt` – Python dependency (Streamlit)

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```
You can also just open `campusfind.html` in any browser.

## Deploy on Streamlit Community Cloud
1. Push this folder to a GitHub repository.
2. Go to https://share.streamlit.io and click **Create app**.
3. Choose your repo and branch, set **Main file path** to `app.py`, then **Deploy**.

## Adding the real campus data
Open `campusfind.html` and edit the script near the top:
- `PLACES` – each place has `id`, `name`, `cat`, `x`, `y`, `info` (map is 800 x 560)
- `J` – invisible junction points on the walkways
- `PATHS` – pairs of ids that are connected by a walkway

The current data is placeholder only and does not match the real campus.

## Future scope
Indoor navigation, QR-code links to locations, voice directions,
multilingual support, an Android app.
