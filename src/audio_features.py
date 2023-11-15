import pandas as pd
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotipy.oauth2 import SpotifyOAuth
# import os
# from dotenv import load_dotenv
# from src import top_tracks

# load_dotenv()

# SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

# scope = "user-library-read user-read-recently-played user-top-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))


def get_audio_features_short_term(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    tracks = [item['name'] for item in results['items']]
    artists = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]

    track_uri = []

    for i in range(limit):
        search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=tracks[i],artist=artists[i]), type='track')
        if search_results['tracks']['items'] == []:
            continue
        track_uri.append(search_results['tracks']['items'][0]['uri'])


    df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
    df.index +=1
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)
    df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
    return df


def get_audio_features_medium_term(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    tracks = [item['name'] for item in results['items']]
    artists = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]

    track_uri = []

    for i in range(limit):
        search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=tracks[i],artist=artists[i]), type='track')
        if search_results['tracks']['items'] == []:
            continue
        track_uri.append(search_results['tracks']['items'][0]['uri'])


    df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
    df.index +=1
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)
    df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
    return df


def get_audio_features_long_term(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    tracks = [item['name'] for item in results['items']]
    artists = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]

    track_uri = []

    for i in range(limit):
        search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=tracks[i],artist=artists[i]), type='track')
        if search_results['tracks']['items'] == []:
            continue
        track_uri.append(search_results['tracks']['items'][0]['uri'])


    df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
    df.index +=1
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)
    df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
    return df

# # Get Audio Features of top tracks (short term)

# def get_audio_features_short_term(spotify):
#     top_short_term_tracks_df = top_tracks.get_top_tracks_short_term_df(spotify)
#     top_tracks_af = top_short_term_tracks_df[['Track', 'Artist']].reset_index()

#     track_uri = []

#     for i in top_tracks_af.index:
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_tracks_af['Track'][i],artist=top_tracks_af['Artist'][i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])

#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df


# # Get Audio Features of top tracks (medium term)

# def get_audio_features_medium_term(spotify):
#     top_medium_term_tracks_df = top_tracks.get_top_tracks_medium_term_df(spotify)
#     top_tracks_af = top_medium_term_tracks_df[['Track', 'Artist']].reset_index()

#     track_uri = []

#     for i in top_tracks_af.index:
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_tracks_af['Track'][i],artist=top_tracks_af['Artist'][i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])

#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df


# # Get Audio Features of top tracks (long term)

# def get_audio_features_long_term(spotify):
#     top_long_term_tracks_df = top_tracks.get_top_tracks_long_term_df(spotify)
#     top_tracks_af = top_long_term_tracks_df[['Track', 'Artist']].reset_index()

#     track_uri = []

#     for i in top_tracks_af.index:
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_tracks_af['Track'][i],artist=top_tracks_af['Artist'][i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])

#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df