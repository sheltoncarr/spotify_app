import pandas as pd

def get_top_artists_short_term_popularity_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]
    popularity_list = [item['popularity'] for item in results['items']]
    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list, "Popularity (Out of 100)": popularity_list})
    df.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index += 1
    return df


def get_top_artists_medium_term_popularity_df(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]
    popularity_list = [item['popularity'] for item in results['items']]
    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list, "Popularity (Out of 100)": popularity_list})
    df.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index += 1
    return df


def get_top_artists_long_term_popularity_df(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]
    popularity_list = [item['popularity'] for item in results['items']]
    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list, "Popularity (Out of 100)": popularity_list})
    df.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index += 1
    return df