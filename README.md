# Spotify Trending 2025

A full-stack app which uses Spotify API that fetches **trending Japanese tracks**(can be changed to another country) by genre.

## Features
- **Genre Search**: Input `jpop`, `rock`, `anime`, `citypop` for top 5 trending songs.
- **Modern UI**: This UI design uses glassmorphism, responsive layout, and Spotify links.
- **JSON API**: `/api/jpop` returns structured data for AI integration.
- **Smart Mapping**: Handles aliases like "rock" → Japanese rock.

## Tech Stack
- **Backend**: Flask + Spotipy (Python)
- **Frontend**: Jinja2 templates + Pure CSS (no frameworks)
- **API**: Spotify Web API (Client Credentials Flow)

- ## How to Setup Locally:
1. Clone: `git clone https://github.com/abdulali123/spotify-trending-2025.git`
2. Install: `pip install -r requirements.txt`
3. Add these 2 below in`.env`:
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

5. Run: `python app.py`
6. Open: http://127.0.0.1:5000


