import pandas as pd
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotipy.oauth2 import SpotifyOAuth
# import os
# from dotenv import load_dotenv
from src import top_artists
from src import top_tracks

# load_dotenv()

# SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

# scope = "user-library-read user-read-recently-played user-top-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))



def get_short_term_track_recs(spotify):
    top_short_term_tracks_df = top_tracks.get_top_tracks_short_term_df(spotify)
    top_5_tracks = top_short_term_tracks_df.head(5)[['Track', 'Artist']]

    track_uri = []

    for i in range(1,6):
        search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_5_tracks['Track'][i],artist=top_5_tracks['Artist'][i]), type='track')
        if search_results['tracks']['items'] == []:
            continue
        track_uri.append(search_results['tracks']['items'][0]['uri'])

    rec_results = spotify.recommendations(seed_tracks = track_uri, limit=10)['tracks']

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for tracks in rec_results:
        track_list.append(tracks['name'])
        for artist in tracks['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(tracks['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(tracks['preview_url'])

    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})
    df.index +=1
    return df



def get_medium_term_track_recs(spotify):
    top_medium_term_tracks_df = top_tracks.get_top_tracks_medium_term_df(spotify)
    top_5_tracks = top_medium_term_tracks_df.head(5)[['Track', 'Artist']]

    track_uri = []

    for i in range(1,6):
        search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_5_tracks['Track'][i],artist=top_5_tracks['Artist'][i]), type='track')
        if search_results['tracks']['items'] == []:
            continue
        track_uri.append(search_results['tracks']['items'][0]['uri'])

    rec_results = spotify.recommendations(seed_tracks = track_uri, limit=10)['tracks']

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for tracks in rec_results:
        track_list.append(tracks['name'])
        for artist in tracks['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(tracks['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(tracks['preview_url'])

    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})
    df.index +=1
    return df



def get_long_term_track_recs(spotify):
    top_long_term_tracks_df = top_tracks.get_top_tracks_long_term_df(spotify)
    top_5_tracks = top_long_term_tracks_df.head(5)[['Track', 'Artist']]

    track_uri = []

    for i in range(1,6):
        search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_5_tracks['Track'][i],artist=top_5_tracks['Artist'][i]), type='track')
        if search_results['tracks']['items'] == []:
            continue
        track_uri.append(search_results['tracks']['items'][0]['uri'])

    rec_results = spotify.recommendations(seed_tracks = track_uri, limit=10)['tracks']

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for tracks in rec_results:
        track_list.append(tracks['name'])
        for artist in tracks['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(tracks['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(tracks['preview_url'])

    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})
    df.index +=1
    return df



def get_short_term_artist_recs(spotify):
    top_short_term_artists_df = top_artists.get_top_artists_short_term_df(spotify)
    top_5_artists = top_short_term_artists_df.head(5)[['Artist']]

    artist_uri = []

    for i in range(1,6):
        search_results = spotify.search(q='artist:{artist}'.format(artist=top_5_artists['Artist'][i]), type='artist')
        artist_uri.append(search_results['artists']['items'][0]['uri'])

    rec_results = spotify.recommendations(seed_artists = artist_uri, limit=10)['tracks']

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for tracks in rec_results:
        track_list.append(tracks['name'])
        for artist in tracks['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(tracks['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(tracks['preview_url'])

    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})
    df.index +=1
    return df



def get_medium_term_artist_recs(spotify):
    top_medium_term_artists_df = top_artists.get_top_artists_medium_term_df(spotify)
    top_5_artists = top_medium_term_artists_df.head(5)[['Artist']]

    artist_uri = []

    for i in range(1,6):
        search_results = spotify.search(q='artist:{artist}'.format(artist=top_5_artists['Artist'][i]), type='artist')
        artist_uri.append(search_results['artists']['items'][0]['uri'])

    rec_results = spotify.recommendations(seed_artists = artist_uri, limit=10)['tracks']

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for tracks in rec_results:
        track_list.append(tracks['name'])
        for artist in tracks['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(tracks['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(tracks['preview_url'])

    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})
    df.index +=1
    return df



def get_long_term_artist_recs(spotify):
    top_long_term_artists_df = top_artists.get_top_artists_long_term_df(spotify)
    top_5_artists = top_long_term_artists_df.head(5)[['Artist']]

    artist_uri = []

    for i in range(1,6):
        search_results = spotify.search(q='artist:{artist}'.format(artist=top_5_artists['Artist'][i]), type='artist')
        artist_uri.append(search_results['artists']['items'][0]['uri'])

    rec_results = spotify.recommendations(seed_artists = artist_uri, limit=10)['tracks']

    track_list = []
    artist_list = []
    artist_list_total = []
    genre_list = []
    audio_sample_list = []

    for tracks in rec_results:
        track_list.append(tracks['name'])
        for artist in tracks['artists']:
            artist_list.append(artist['name'])
        artist_list_total.append(', '.join(artist_list))
        artist_list = []
        genre_list.append(', '.join(spotify.artist(tracks['artists'][0]["external_urls"]["spotify"])['genres']).title())
        audio_sample_list.append(tracks['preview_url'])

    df = pd.DataFrame({'Track':track_list,
                       'Artist':artist_list_total,
                       'Genre':genre_list,
                       'Audio Sample':audio_sample_list})
    df.index +=1
    return df