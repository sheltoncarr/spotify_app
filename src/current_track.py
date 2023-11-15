import pandas as pd

def get_current_track(spotify):
    result = spotify.current_user_playing_track()

    track = result['item']['name']
    album = result['item']['album']['name']
    artist_list = ', '.join(artist['name'] for artist in result['item']['artists'])
    artist_id = result['item']['artists'][0]['id']
    artist_info = spotify.artist(artist_id)
    genre_list = ', '.join(artist_info['genres'][:3]).title()
    audio_sample = result['item']['preview_url']

    df = pd.DataFrame({
        'Track': [track],
        'Album': [album],
        'Artist': [artist_list],
        'Genre': [genre_list],
        'Audio Sample': [audio_sample]
    })

    df.index += 1
    return df