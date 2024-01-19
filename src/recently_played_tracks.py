import pandas as pd
from datetime import datetime
import re

def most_recently_played_tracks(spotify, limit=50):

    """
    Get the most recently played tracks for a user
    
    Args:
        spotify: User authorization
        limit: Number of recent tracks to include

    Returns: A dataframe of tracks, albums, artists, genres, release dates, and audio samples for the user's 50 most recently played tracks
    """

    results = spotify.current_user_recently_played(limit=limit)

    track_list = [item['track']['name'] for item in results['items']]
    album_list = [item['track']['album']['name'] for item in results['items']]
    artist_list = [', '.join(artist['name'] for artist in item['track']['artists']) for item in results['items']]
    artist_id = [item['track']['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    release_date = [item['track']['album']['release_date'] for item in results['items']]
    release_date_list = []
    for date in release_date:
        if len(date) == 10: # if format is yyyy-mm-dd
            if re.compile(r'\d{4}-05-\d{2}').search(date):
                date = datetime.strptime(date, "%Y-%m-%d").strftime("%b %-d, %Y")
            else:
                date = datetime.strptime(date, "%Y-%m-%d").strftime("%b. %-d, %Y")
            release_date_list.append(date)
        elif len(date) == 7: # if format is yyyy-mm
            if re.compile(r'\d{4}-05').search(date):
                date = datetime.strptime(date, "%Y-%m").strftime("%b %Y")
            else:
                date = datetime.strptime(date, "%Y-%m").strftime("%b. %Y")
            release_date_list.append(date)
        else: # if format is yyyy
            release_date_list.append(date)
    audio_sample_list = [item['track']['preview_url'] for item in results['items']]
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