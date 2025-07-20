import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# from pprint import pprint

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")

# ------------------------- SCRAPING BILLBOARD -------------------------

target_date = input(
    "Which year do you want to travel to?  Type the date in this format YYYY-MM-DD: "
)
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

url = f"https://www.billboard.com/charts/hot-100/{target_date}/"

response = requests.get(url=url, headers=header)
billboard_html_content = response.text
soup = BeautifulSoup(billboard_html_content, "html.parser")
song_name_tags = soup.select(selector="li h3")
song_names = [tag.getText().strip() for tag in song_name_tags][:100]
print(song_names)

# ------------------------- SPOTIFY AUTHORIZATION -------------------------

scope = "playlist-modify-public"

auth_manager = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri="https://example.com/callback",  # 任意で設定、Spotify Dashboardと一致させる
    scope=scope,
)

# ------------------------- CREATING A NEW PLAYLIST AT SPOTIFY -------------------------

sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]
playlist_name = f"Billboard-Hot-100-{target_date}"
playlist_description = f"Top 100 music for {target_date}"
public_playlist = True

new_playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=public_playlist,
    description=playlist_description,
)

playlist_id = new_playlist["id"]
print(f"Playlist '{playlist_name}' created with ID: {playlist_id}")

for song in song_names:
    track_params = f"track:{song} year:{target_date[:4]}"
    track_results = sp.search(q=track_params, type="track")
    try:
        track_uri = track_results["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id=playlist_id, items=[track_uri])
        print(f"Added track to playlist: {track_uri}")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
