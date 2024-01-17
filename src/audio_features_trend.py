import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('agg')

def get_audio_features_short_term(spotify, limit=50, time_range='short_term'):

    """
    Get average audio feature values of user's top 50 songs in the short-term
    
    Args:
        spotify: User authorization
        limit: Number of top songs to include in calculation
        time_range: Over what time frame to pull user's top songs

    Returns: A dataframe of audio features and their average values for the user's top 50 songs over the short-term
    """

    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    df = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)*100
    df = pd.DataFrame({'Audio Feature':df.index, 'Average Value':df.values})
    df['Audio Feature'] = df['Audio Feature'].str.title()
    df['Average Value'] = df['Average Value'].astype(int)
    df.index += 1
    return df


def get_audio_features_medium_term(spotify, limit=50, time_range='medium_term'):

    """
    Get average audio feature values of user's top 50 songs in the medium-term
    
    Args:
        spotify: User authorization
        limit: Number of top songs to include in calculation
        time_range: Over what time frame to pull user's top songs

    Returns: A dataframe of audio features and their average values for the user's top 50 songs over the medium-term
    """

    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    df = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)*100
    df = pd.DataFrame({'Audio Feature':df.index, 'Average Value':df.values})
    df['Audio Feature'] = df['Audio Feature'].str.title()
    df['Average Value'] = df['Average Value'].astype(int)
    df.index += 1
    return df


def get_audio_features_long_term(spotify, limit=50, time_range='long_term'):

    """
    Get average audio feature values of user's top 50 songs in the long-term
    
    Args:
        spotify: User authorization
        limit: Number of top songs to include in calculation
        time_range: Over what time frame to pull user's top songs

    Returns: A dataframe of audio features and their average values for the user's top 50 songs over the long-term
    """

    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    df = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)*100
    df = pd.DataFrame({'Audio Feature':df.index, 'Average Value':df.values})
    df['Audio Feature'] = df['Audio Feature'].str.title()
    df['Average Value'] = df['Average Value'].astype(int)
    df.index += 1
    return df


def merge_audio_features_df(spotify):

    """
    Merge average audio feature values of user's top 50 songs over all time frames
    
    Args:
        spotify: User authorization

    Returns: A dataframe of audio features and their average values for the user's top 50 songs over all time frames
    """

    short = get_audio_features_short_term(spotify)
    medium = get_audio_features_medium_term(spotify)
    long = get_audio_features_long_term(spotify)
    result = pd.merge(long, medium, on='Audio Feature').merge(short, on='Audio Feature')
    result.rename(columns={'Average Value_x':'Long Term','Average Value_y':'Medium Term','Average Value':'Short Term'}, inplace=True)
    return result


def audio_features_trend(spotify):

    """
    Visualize average audio feature values of user's top 50 songs over all time frames
    
    Args:
        spotify: User authorization

    Returns: A line chart of audio features and their average values for the user's top 50 songs over all time frames
    """

    result = merge_audio_features_df(spotify)

    plt.figure(figsize=(7.5, 8), facecolor='#1ED760')

    for feature in result['Audio Feature']:
        values = result[result['Audio Feature'] == feature].values.flatten()[1:]
        plt.plot(result.columns[1:], values, label=feature, marker='o', linewidth=3)

        # Adding data labels
        for i, value in enumerate(values):
            plt.annotate(f'{int(value)}', (i, value), textcoords="offset points", xytext=(0,7), ha='center')


    plt.title('Audio Feature Trends Over Time', fontsize=20, y=1.15)
    plt.xlabel('Time Range', fontsize=15, labelpad=15)
    plt.ylabel('Average Value', fontsize=15)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, shadow=True, title='Audio Feature')
    plt.grid(axis='y', linewidth=0.25)
    plt.tight_layout()

    plt.savefig('static/images/audio_feature_trend.png', bbox_inches='tight', dpi=300)
    
    plt.close()
