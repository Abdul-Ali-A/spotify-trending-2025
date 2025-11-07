import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Testing:
print("Client ID:", client_id[:5] + "..." if client_id else "MISSING!")
print("Client Secret:", "Loaded" if client_secret else "MISSING!")

# Error prevention if the Client ID is not loaded.
if not client_id or not client_secret:
    raise EnvironmentError(
        "SPOTIPY_CLIENT_ID or SPOTIPY_CLIENT_SECRET is missing! "
    )

# Connecting to Spotify
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_popular_tracks(genre: str, limit: int = 8):
    if limit > 50:
        limit = 50

    genre_map = {
        'jpop': 'j-pop OR neo j-pop OR gacha pop',
        'jrock': 'j-rock OR japanese rock OR visual kei',
        'rock': 'j-rock OR japanese rock OR visual kei',  # ← NEW!
        'anime': 'anison OR anime OR vocaloid OR anisong',
        'citypop': 'city pop OR japanese 80s pop OR vaporwave',
        'jhiphop': 'j-hip hop OR japanese hip hop OR desi hip hop',
        'jazz': 'japanese jazz OR nu jazz OR jazz fusion',
        'enka': 'enka OR japanese ballad OR kayokyoku',
        'vocaloid': 'vocaloid OR hatsune miku OR utau',
        'idol': 'j-idol OR japanese idol pop OR akb48',
        'visualkei': 'visual kei OR j-rock OR gothic rock'
    }
    query = genre_map.get(genre.lower(), genre) # .get(key,value)

    # Error prevention after the search.
    try:
        track_results = sp.search(q=query, type='track', limit=limit, market='JP')
    except Exception as e:
        print("Spotify API Error:", e)
        return []

    tracks = []
    for track in track_results['tracks']['items']:
        tracks.append({
            "name": track['name'],
            "artist": ', '.join([a['name'] for a in track['artists']]),
            "album": track['album']['name'],
            "popularity": track['popularity'],
            'link': track['external_urls']['spotify']
        })

    tracks.sort(key=lambda x: x['popularity'], reverse=True)
    return tracks[:limit]