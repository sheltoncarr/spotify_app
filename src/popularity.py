import pandas as pd

def get_top_artists_short_term_popularity_df(spotify, limit=50, time_range='short_term'):

    """
    Get the popularity score (out of 100) of each of the user's top 50 artists in the short-term
    
    Args:
        spotify: User authorization
        limit: Number of top artists to include
        time_range: Over what time frame to pull user's top artists

    Returns: A dataframe of artists, genres, and popularity scores for the user's top 50 artists in the short-term
    """

    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]
    popularity_list = [item['popularity'] for item in results['items']]
    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list, "Popularity (Out of 100)": popularity_list})
    df.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Popularity (Out of 100)"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler


def get_top_artists_medium_term_popularity_df(spotify, limit=50, time_range='medium_term'):

    """
    Get the popularity score (out of 100) of each of the user's top 50 artists in the medium-term
    
    Args:
        spotify: User authorization
        limit: Number of top artists to include
        time_range: Over what time frame to pull user's top artists

    Returns: A dataframe of artists, genres, and popularity scores for the user's top 50 artists in the medium-term
    """

    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]
    popularity_list = [item['popularity'] for item in results['items']]
    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list, "Popularity (Out of 100)": popularity_list})
    df.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Popularity (Out of 100)"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler


def get_top_artists_long_term_popularity_df(spotify, limit=50, time_range='long_term'):

    """
    Get the popularity score (out of 100) of each of the user's top 50 artists in the long-term
    
    Args:
        spotify: User authorization
        limit: Number of top artists to include
        time_range: Over what time frame to pull user's top artists

    Returns: A dataframe of artists, genres, and popularity scores for the user's top 50 artists in the long-term
    """

    results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    artist_list = [item['name'] for item in results['items']]
    genre_list = [', '.join(item['genres'][:3]).title() for item in results['items']]
    popularity_list = [item['popularity'] for item in results['items']]
    df = pd.DataFrame({'Artist': artist_list, 'Genre': genre_list, "Popularity (Out of 100)": popularity_list})
    df.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df.reset_index(drop=True,inplace=True)
    df.index += 1
    dfStyler = (
        df.style
        .set_properties(subset=["Popularity (Out of 100)"], **{'text-align': 'center'})
        .set_table_styles([{"selector": "td, th", "props": [("border", "1px solid grey !important")]}])
    )
    return dfStyler