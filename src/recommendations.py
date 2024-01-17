import pandas as pd
from datetime import datetime

def get_short_term_track_recs(spotify, limit=5, time_range='short_term'):

    """
    Get song recommendations based on the user's top 5 songs in the short-term
    
    Args:
        spotify: User authorization
        limit: Number of song recommendations to return
        time_range: Over what time frame to pull user's top songs

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's song recommendations over the short-term
    """

    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_tracks=track_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in rec_results]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mmm-dd
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else 'N/A' for url in audio_sample_list
    ]
    
    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Release Date': release_date_list,
        'Audio Sample': play_button
    })

    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Audio Sample"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler



def get_medium_term_track_recs(spotify, limit=5, time_range='medium_term'):

    """
    Get song recommendations based on the user's top 5 songs in the medium-term
    
    Args:
        spotify: User authorization
        limit: Number of song recommendations to return
        time_range: Over what time frame to pull user's top songs

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's song recommendations over the medium-term
    """

    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_tracks=track_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in rec_results]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mmm-dd
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else 'N/A' for url in audio_sample_list
    ]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Release Date': release_date_list,
        'Audio Sample': play_button
    })

    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Audio Sample"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler



def get_long_term_track_recs(spotify, limit=5, time_range='long_term'):

    """
    Get song recommendations based on the user's top 5 songs in the long-term
    
    Args:
        spotify: User authorization
        limit: Number of song recommendations to return
        time_range: Over what time frame to pull user's top songs

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's song recommendations over the long-term
    """

    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_tracks=track_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in rec_results]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mmm-dd
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else 'N/A' for url in audio_sample_list
    ]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Release Date': release_date_list,
        'Audio Sample': play_button
    })

    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Audio Sample"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler


def get_short_term_artist_recs(spotify, limit=5, time_range='short_term'):

    """
    Get song recommendations based on the user's top 5 artists in the short-term
    
    Args:
        spotify: User authorization
        limit: Number of song recommendations to return
        time_range: Over what time frame to pull user's top artists

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's song recommendations over the short-term
    """

    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_artists=artist_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in rec_results]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mmm-dd
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else 'N/A' for url in audio_sample_list
    ]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Release Date': release_date_list,
        'Audio Sample': play_button
    })

    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Audio Sample"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler


def get_medium_term_artist_recs(spotify, limit=5, time_range='medium_term'):

    """
    Get song recommendations based on the user's top 5 artists in the medium-term
    
    Args:
        spotify: User authorization
        limit: Number of song recommendations to return
        time_range: Over what time frame to pull user's top artists

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's song recommendations over the medium-term
    """

    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_artists=artist_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in rec_results]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mmm-dd
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else 'N/A' for url in audio_sample_list
    ]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Release Date': release_date_list,
        'Audio Sample': play_button
    })

    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Audio Sample"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler



def get_long_term_artist_recs(spotify, limit=5, time_range='long_term'):

    """
    Get song recommendations based on the user's top 5 artists in the long-term
    
    Args:
        spotify: User authorization
        limit: Number of song recommendations to return
        time_range: Over what time frame to pull user's top artists

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's song recommendations over the long-term
    """

    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_artists=artist_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in rec_results]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mmm-dd
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else 'N/A' for url in audio_sample_list
    ]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Release Date': release_date_list,
        'Audio Sample': play_button
    })

    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Audio Sample"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler