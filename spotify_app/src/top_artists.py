import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

scope = "user-library-read user-read-recently-played user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))



def get_top_artists_short_term_df(limit=50, time_range='short_term'):
    results = sp.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = []
    genre_list = []
    for idx, item in enumerate(results['items']):
        artist_list.append(item['name'])
        genre_list.append(', '.join(item['genres']).title())

    top_artists_short_term_df = pd.DataFrame({'Artist':artist_list,
                                              'Genre':genre_list})
    top_artists_short_term_df.index += 1
    return top_artists_short_term_df



def get_top_artists_medium_term_df(limit=50, time_range='medium_term'):
    results = sp.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = []
    genre_list = []
    for idx, item in enumerate(results['items']):
        artist_list.append(item['name'])
        genre_list.append(', '.join(item['genres']).title())

    top_artists_medium_term_df = pd.DataFrame({'Artist':artist_list,
                                              'Genre':genre_list})
    top_artists_medium_term_df.index += 1
    return top_artists_medium_term_df



def get_top_artists_long_term_df(limit=50, time_range='long_term'):
    results = sp.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = []
    genre_list = []
    for idx, item in enumerate(results['items']):
        artist_list.append(item['name'])
        genre_list.append(', '.join(item['genres']).title())

    top_artists_long_term_df = pd.DataFrame({'Artist':artist_list,
                                              'Genre':genre_list})
    top_artists_long_term_df.index += 1
    return top_artists_long_term_df