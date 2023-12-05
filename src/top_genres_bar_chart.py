import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def get_top_genres_short_term_df(spotify, limit=50, time_range='short_term'):
    artist_results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    track_results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    artist_genre_list = [item['genres'] for item in artist_results['items']]
    artist_genre_list = [genre for sublist in artist_genre_list for genre in sublist]

    artist_id = [item['artists'][0]['id'] for item in track_results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    track_genre_list = [artist['genres'] for artist in artist_info]
    track_genre_list = [genre for sublist in track_genre_list for genre in sublist]

    genre_list = artist_genre_list + track_genre_list
    genre_list = [genre.title() for genre in genre_list]

    genre_count = Counter(genre_list)

    df = pd.DataFrame(list(genre_count.items()), columns=['Genre', 'Count of Top Artists/Tracks'])
    df.sort_values(by=['Count of Top Artists/Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df


def get_top_genres_medium_term_df(spotify, limit=50, time_range='medium_term'):
    artist_results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    track_results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    artist_genre_list = [item['genres'] for item in artist_results['items']]
    artist_genre_list = [genre for sublist in artist_genre_list for genre in sublist]

    artist_id = [item['artists'][0]['id'] for item in track_results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    track_genre_list = [artist['genres'] for artist in artist_info]
    track_genre_list = [genre for sublist in track_genre_list for genre in sublist]

    genre_list = artist_genre_list + track_genre_list
    genre_list = [genre.title() for genre in genre_list]

    genre_count = Counter(genre_list)

    df = pd.DataFrame(list(genre_count.items()), columns=['Genre', 'Count of Top Artists/Tracks'])
    df.sort_values(by=['Count of Top Artists/Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df


def get_top_genres_long_term_df(spotify, limit=50, time_range='long_term'):
    artist_results = spotify.current_user_top_artists(limit=limit, time_range=time_range)
    track_results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    
    artist_genre_list = [item['genres'] for item in artist_results['items']]
    artist_genre_list = [genre for sublist in artist_genre_list for genre in sublist]

    artist_id = [item['artists'][0]['id'] for item in track_results['items']]
    artist_info = spotify.artists(artist_id)['artists']
    track_genre_list = [artist['genres'] for artist in artist_info]
    track_genre_list = [genre for sublist in track_genre_list for genre in sublist]

    genre_list = artist_genre_list + track_genre_list
    genre_list = [genre.title() for genre in genre_list]

    genre_count = Counter(genre_list)

    df = pd.DataFrame(list(genre_count.items()), columns=['Genre', 'Count of Top Artists/Tracks'])
    df.sort_values(by=['Count of Top Artists/Tracks'], inplace=True, ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    return df



def top_genres_bar_chart(spotify):

    df_short = get_top_genres_short_term_df(spotify)[:20]
    df_medium = get_top_genres_medium_term_df(spotify)[:20]
    df_long = get_top_genres_long_term_df(spotify)[:20]

    df_short = df_short.sort_values(by="Count of Top Artists/Tracks", ascending=True)
    df_medium = df_medium.sort_values(by="Count of Top Artists/Tracks", ascending=True)
    df_long = df_long.sort_values(by="Count of Top Artists/Tracks", ascending=True)

    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(8, 16), facecolor='#1ED760')

    dataframes = [df_short, df_medium, df_long]
    titles = ['Short Term (Last 4 Weeks)', 'Medium Term (Last 6 Months)', 'Long Term (Last Several Years)']

    for i, (ax, df, title) in enumerate(zip(axs, dataframes, titles)):
        bars = ax.barh(y=df["Genre"], width=df["Count of Top Artists/Tracks"])

        # Add data labels above each bar
        for bar in bars:
            ax.text(bar.get_width() + 0.05,
                    bar.get_y() + bar.get_height()/2,
                    f'{bar.get_width():,.0f}', 
                    va='center', ha='left', fontsize=10)

        # Customize the plot if needed
        ax.set_title(f"Top Genres - {title}", fontsize=15)
        ax.set_xlabel("Count of Top Artists/Tracks", fontsize=12)
        ax.set_ylabel("Genre", fontsize=12)
        ax.grid(axis='x', linewidth=0.25)

    plt.tight_layout()

    # write image to static png
    plt.savefig('static/images/top_genres_bar_chart.png', bbox_inches='tight', dpi=300)

    plt.close()