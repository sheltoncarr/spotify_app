import pandas as pd
from collections import Counter


def get_top_genres_short_term_df(spotify, limit=50, time_range='short_term'):

    """
    Get user's top genres based on their top 50 songs and artists in the short-term
    
    Args:
        spotify: User authorization
        limit: Number of top songs/artists to include in calculation
        time_range: Over what time frame to pull user's top songs/artists

    Returns: A dataframe containing a count of top tracks/artists by genre based on the user's top 50 songs/artists over the short-term
    """

    artist_results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    track_results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    artist_genre_list = [item['genres'] for item in artist_results['items']]
    artist_genre_list = [genre for sublist in artist_genre_list for genre in sublist]

    artist_id = [item['artists'][0]['id'] for item in track_results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    track_genre_list = [artist['genres'] for artist in artist_info]
    track_genre_list = [genre for sublist in track_genre_list for genre in sublist]

    genre_list = artist_genre_list + track_genre_list
    genre_list = [genre.title() for genre in genre_list]

    genre_count = Counter(genre_list)

    df = pd.DataFrame(list(genre_count.items()), columns=['Genre', 'Count of Top Artists/Tracks'])
    df.sort_values(by=['Count of Top Artists/Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df


def get_top_genres_medium_term_df(spotify, limit=50, time_range='medium_term'):

    """
    Get user's top genres based on their top 50 songs and artists in the medium-term
    
    Args:
        spotify: User authorization
        limit: Number of top songs/artists to include in calculation
        time_range: Over what time frame to pull user's top songs/artists

    Returns: A dataframe containing a count of top tracks/artists by genre based on the user's top 50 songs/artists over the medium-term
    """

    artist_results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    track_results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    artist_genre_list = [item['genres'] for item in artist_results['items']]
    artist_genre_list = [genre for sublist in artist_genre_list for genre in sublist]

    artist_id = [item['artists'][0]['id'] for item in track_results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    track_genre_list = [artist['genres'] for artist in artist_info]
    track_genre_list = [genre for sublist in track_genre_list for genre in sublist]

    genre_list = artist_genre_list + track_genre_list
    genre_list = [genre.title() for genre in genre_list]

    genre_count = Counter(genre_list)

    df = pd.DataFrame(list(genre_count.items()), columns=['Genre', 'Count of Top Artists/Tracks'])
    df.sort_values(by=['Count of Top Artists/Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df


def get_top_genres_long_term_df(spotify, limit=50, time_range='long_term'):

    """
    Get user's top genres based on their top 50 songs and artists in the long-term
    
    Args:
        spotify: User authorization
        limit: Number of top songs/artists to include in calculation
        time_range: Over what time frame to pull user's top songs/artists

    Returns: A dataframe containing a count of top tracks/artists by genre based on the user's top 50 songs/artists over the long-term
    """

    artist_results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    track_results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    artist_genre_list = [item['genres'] for item in artist_results['items']]
    artist_genre_list = [genre for sublist in artist_genre_list for genre in sublist]

    artist_id = [item['artists'][0]['id'] for item in track_results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    track_genre_list = [artist['genres'] for artist in artist_info]
    track_genre_list = [genre for sublist in track_genre_list for genre in sublist]

    genre_list = artist_genre_list + track_genre_list
    genre_list = [genre.title() for genre in genre_list]

    genre_count = Counter(genre_list)

    df = pd.DataFrame(list(genre_count.items()), columns=['Genre', 'Count of Top Artists/Tracks'])
    df.sort_values(by=['Count of Top Artists/Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df