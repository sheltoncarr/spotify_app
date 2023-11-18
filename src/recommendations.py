import pandas as pd

def get_short_term_track_recs(spotify, limit=5, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_tracks=track_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Audio Sample': audio_sample_list
    })
    df.index += 1
    return df



def get_medium_term_track_recs(spotify, limit=5, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_tracks=track_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Audio Sample': audio_sample_list
    })
    df.index += 1
    return df



def get_long_term_track_recs(spotify, limit=5, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_tracks=track_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]

    df = pd.DataFrame({
        'Track': track_list,
        'Album': album_list,
        'Artist': artist_list,
        'Genre': genre_list,
        'Audio Sample': audio_sample_list
    })
    df.index += 1
    return df



def get_short_term_artist_recs(spotify, limit=5, time_range='short_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_artists=artist_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]

    df = pd.DataFrame({'Track': track_list,
                       'Album': album_list,
                       'Artist': artist_list,
                       'Genre': genre_list,
                       'Audio Sample': audio_sample_list})
    df.index += 1
    return df



def get_medium_term_artist_recs(spotify, limit=5, time_range='medium_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_artists=artist_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]

    df = pd.DataFrame({'Track': track_list,
                       'Album': album_list,
                       'Artist': artist_list,
                       'Genre': genre_list,
                       'Audio Sample': audio_sample_list})
    df.index += 1
    return df



def get_long_term_artist_recs(spotify, limit=5, time_range='long_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_uri_list = [item['id'] for item in results['items']]

    rec_results = spotify.recommendations(seed_artists=artist_uri_list, limit=10)['tracks']

    track_list = [tracks['name'] for tracks in rec_results]
    album_list = [item['album']['name'] for item in rec_results]
    artist_list = [', '.join(artist['name'] for artist in tracks['artists']) for tracks in rec_results]
    artist_id = [item['artists'][0]['id'] for item in rec_results]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [tracks['preview_url'] for tracks in rec_results]

    df = pd.DataFrame({'Track': track_list,
                       'Album': album_list,
                       'Artist': artist_list,
                       'Genre': genre_list,
                       'Audio Sample': audio_sample_list})
    df.index += 1
    return df