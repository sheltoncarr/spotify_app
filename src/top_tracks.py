import pandas as pd
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotipy.oauth2 import SpotifyOAuth
# import os
# from dotenv import load_dotenv

# load_dotenv()

# SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

# scope = "user-library-read user-read-recently-played user-top-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))

# Potentially better code:

def get_top_tracks_short_term_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    artist_list_total = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres']).title() for artist in artist_info]
    audio_sample_list = [item['preview_url'] for item in results['items']]

    df = pd.DataFrame({
        'Track': track_list,
        'Artist': artist_list_total,
        'Genre': genre_list,
        'Audio Sample': audio_sample_list
    })

    df.index += 1
    return df



def get_top_tracks_medium_term_df(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    artist_list_total = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres']).title() for artist in artist_info]
    audio_sample_list = [item['preview_url'] for item in results['items']]

    df = pd.DataFrame({
        'Track': track_list,
        'Artist': artist_list_total,
        'Genre': genre_list,
        'Audio Sample': audio_sample_list
    })

    df.index += 1
    return df



def get_top_tracks_long_term_df(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    artist_list_total = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres']).title() for artist in artist_info]
    audio_sample_list = [item['preview_url'] for item in results['items']]

    df = pd.DataFrame({
        'Track': track_list,
        'Artist': artist_list_total,
        'Genre': genre_list,
        'Audio Sample': audio_sample_list
    })

    df.index += 1
    return df