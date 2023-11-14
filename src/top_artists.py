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

def get_top_artists_short_term_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]

    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list})
    df.index += 1
    return df



def get_top_artists_medium_term_df(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]

    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list})
    df.index += 1
    return df



def get_top_artists_long_term_df(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]

    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list})
    df.index += 1
    return df


# def get_top_artists_short_term_df(spotify, limit=50, time_range='short_term'):
#     results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
#     artist_list = []
#     genre_list = []
#     for idx, item in enumerate(results['items']):
#         artist_list.append(item['name'])
#         genre_list.append(', '.join(item['genres']).title())

#     df = pd.DataFrame({'Artist':artist_list,
#                        'Genre':genre_list})
#     df.index += 1
#     return df



# def get_top_artists_medium_term_df(spotify, limit=50, time_range='medium_term'):
#     results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
#     artist_list = []
#     genre_list = []
#     for idx, item in enumerate(results['items']):
#         artist_list.append(item['name'])
#         genre_list.append(', '.join(item['genres']).title())

#     df = pd.DataFrame({'Artist':artist_list,
#                        'Genre':genre_list})
#     df.index += 1
#     return df



# def get_top_artists_long_term_df(spotify, limit=50, time_range='long_term'):
#     results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
#     artist_list = []
#     genre_list = []
#     for idx, item in enumerate(results['items']):
#         artist_list.append(item['name'])
#         genre_list.append(', '.join(item['genres']).title())

#     df = pd.DataFrame({'Artist':artist_list,
#                        'Genre':genre_list})
#     df.index += 1
#     return df