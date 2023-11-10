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



def get_top_tracks_short_term_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for idx, item in enumerate(results['items']):
        track_list.append(item['name'])
        for artist in item['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(item['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(item['preview_url'])


    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})

    df.index += 1
    return df



def get_top_tracks_medium_term_df(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for idx, item in enumerate(results['items']):
        track_list.append(item['name'])
        for artist in item['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(item['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(item['preview_url'])


    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})

    df.index += 1
    return df



def get_top_tracks_long_term_df(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for idx, item in enumerate(results['items']):
        track_list.append(item['name'])
        for artist in item['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(item['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(item['preview_url'])


    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})

    df.index += 1
    return df