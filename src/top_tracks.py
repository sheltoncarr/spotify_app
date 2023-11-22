import pandas as pd
from datetime import datetime

def get_top_tracks_short_term_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    album_list = [item['album']['name'] for item in results['items']]
    artist_list = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in results['items']]
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
    audio_sample_list = [item['preview_url'] for item in results['items']]
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
    return df



def get_top_tracks_medium_term_df(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    album_list = [item['album']['name'] for item in results['items']]
    artist_list = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in results['items']]
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
    audio_sample_list = [item['preview_url'] for item in results['items']]
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
    return df



def get_top_tracks_long_term_df(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    album_list = [item['album']['name'] for item in results['items']]
    artist_list = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['album']['release_date'] for item in results['items']]
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
    audio_sample_list = [item['preview_url'] for item in results['items']]
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
    return df