import pandas as pd

def most_recently_played_tracks(spotify, limit=50):
    results = spotify.current_user_recently_played(limit=limit)

    track_list = [item['track']['name'] for item in results['items']]
    album_list = [item['track']['album']['name'] for item in results['items']]
    artist_list = [', '.join(artist['name'] for artist in item['track']['artists']) for item in results['items']]
    artist_id = [item['track']['artists'][0]['id'] for item in results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    genre_list = [', '.join(artist['genres'][:3]).title() for artist in artist_info]
    audio_sample_list = [item['track']['preview_url'] for item in results['items']]
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