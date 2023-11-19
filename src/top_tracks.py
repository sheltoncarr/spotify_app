import pandas as pd

def get_top_tracks_short_term_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    track_list = [item['name'] for item in results['items']]
    album_list = [item['album']['name'] for item in results['items']]
    artist_list = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]
    artist_id = [item['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [item['preview_url'] for item in results['items']]
    play_button = ['<button class="play-button" onclick="playAudio(\'' + url + '\')">Play</button>' if url else '' for url in audio_sample_list]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
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
    audio_sample_list = [item['preview_url'] for item in results['items']]
    play_button = ['<button class="play-button" onclick="playAudio(\'' + url + '\')">Play</button>' if url else '' for url in audio_sample_list]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
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
    audio_sample_list = [item['preview_url'] for item in results['items']]
    play_button = ['<button class="play-button" onclick="playAudio(\'' + url + '\')">Play</button>' if url else '' for url in audio_sample_list]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Audio Sample': play_button
    })

    df.index += 1
    return df