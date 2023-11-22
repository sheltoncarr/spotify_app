import pandas as pd
from collections import Counter

def get_top_years_short_term_df(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    release_date_list = [item['album']['release_date'] for item in results['items']]
    release_year_list = []
    for track_release_date in release_date_list:
        release_year_list.append(track_release_date[:4])
    release_year_count = Counter(release_year_list)

    df = pd.DataFrame(list(release_year_count.items()), columns=['Year', 'Count of Top Tracks'])
    df.sort_values(by=['Count of Top Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df


def get_top_years_medium_term_df(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    release_date_list = [item['album']['release_date'] for item in results['items']]
    release_year_list = []
    for track_release_date in release_date_list:
        release_year_list.append(track_release_date[:4])
    release_year_count = Counter(release_year_list)

    df = pd.DataFrame(list(release_year_count.items()), columns=['Year', 'Count of Top Tracks'])
    df.sort_values(by=['Count of Top Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df


def get_top_years_long_term_df(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    release_date_list = [item['album']['release_date'] for item in results['items']]
    release_year_list = []
    for track_release_date in release_date_list:
        release_year_list.append(track_release_date[:4])
    release_year_count = Counter(release_year_list)

    df = pd.DataFrame(list(release_year_count.items()), columns=['Year', 'Count of Top Tracks'])
    df.sort_values(by=['Count of Top Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df