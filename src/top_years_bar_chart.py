import matplotlib.pyplot as plt
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



def top_years_bar_chart(spotify):

    df_short = get_top_years_short_term_df(spotify)[:10]
    df_medium = get_top_years_medium_term_df(spotify)[:10]
    df_long = get_top_years_long_term_df(spotify)[:10]

    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(8, 16), facecolor='#1ED760')

    dataframes = [df_short, df_medium, df_long]
    titles = ['Short Term (Last 4 Weeks)', 'Medium Term (Last 6 Months)', 'Long Term (Last Several Years)']

    for i, (ax, df, title) in enumerate(zip(axs, dataframes, titles)):
        bars = ax.bar(x=df["Year"], height=df["Count of Top Tracks"])

        # Add data labels above each bar
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    f'{bar.get_height():,.0f}',
                    ha='center', va='bottom', fontsize=10)

        # Customize the plot if needed
        ax.set_title(f"Top Years - {title}", fontsize=15)
        ax.set_xlabel("Release Year", fontsize=12)
        ax.set_xticks(df["Year"])
        ax.tick_params(axis='x', rotation=30)
        ax.set_ylabel("Count of Top Tracks", fontsize=12)
        ax.grid(axis='y', linewidth=0.25)

    plt.tight_layout()

    # write image to static png
    plt.savefig('static/images/top_years_bar_chart.png', bbox_inches='tight', dpi=300)
    
    # plt.show()
    plt.close()