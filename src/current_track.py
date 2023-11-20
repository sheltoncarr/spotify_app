import pandas as pd

def get_current_track(spotify):
    result = spotify.current_user_playing_track()

    track = result['item']['name']
    album = result['item']['album']['name']
    artist_list = ', '.join(artist['name'] for artist in result['item']['artists'])
    artist_id = result['item']['artists'][0]['id']
    artist_info = spotify.artist(artist_id)
    genre_list = ', '.join(artist_info['genres'][:3]).title()
    play_button = [
        f'<button class="play-button" onclick="togglePlayPause(this, \'{url}\')">'
        f'<i class="play-pause-icon fas fa-play"></i></button>'
        if url else '' for url in audio_sample_list
    ]

    df = pd.DataFrame({
        'Track': [track],
        'Album': [album],
        'Artist': [artist_list],
        'Genre': [genre_list],
        'Audio Sample': [play_button]
    })

    df.index += 1
    return df