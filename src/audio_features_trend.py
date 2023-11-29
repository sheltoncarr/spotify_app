import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
# import audio_features
import plotly.io as pio
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('agg')

# load_dotenv()

# SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

# scope = "user-library-read user-read-recently-played user-top-read"

# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))


def get_audio_features_short_term(spotify, limit=50, time_range='short_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    df = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)
    df = pd.DataFrame({'Audio Feature':df.index, 'Average Value':df.values})
    df['Audio Feature'] = df['Audio Feature'].str.title()
    df.index += 1
    return df


def get_audio_features_medium_term(spotify, limit=50, time_range='medium_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    df = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)
    df = pd.DataFrame({'Audio Feature':df.index, 'Average Value':df.values})
    df['Audio Feature'] = df['Audio Feature'].str.title()
    df.index += 1
    return df


def get_audio_features_long_term(spotify, limit=50, time_range='long_term'):
    results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
    track_uri_list = [item['id'] for item in results['items']]

    df = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
    df = df.drop(columns=drop_columns)
    df = df.mean(axis=0)
    df = pd.DataFrame({'Audio Feature':df.index, 'Average Value':df.values})
    df['Audio Feature'] = df['Audio Feature'].str.title()
    df.index += 1
    return df


def merge_audio_features_df(spotify):
    short = get_audio_features_short_term(spotify)
    medium = get_audio_features_medium_term(spotify)
    long = get_audio_features_long_term(spotify)
    result = pd.merge(long, medium, on='Audio Feature').merge(short, on='Audio Feature')
    result.rename(columns={'Average Value_x':'Long Term','Average Value_y':'Medium Term','Average Value':'Short Term'}, inplace=True)
    return result



# def audio_features_trend(spotify):
#     fig, ax = plt.subplots()
#     ax.plot([1, 2, 3], [4, 5, 6])

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)

#     plot_data = base64.b64encode(buffer.read()).decode('utf-8')
#     html_img_tag = f'<img src="data:image/png;base64,{plot_data}" alt="Matplotlib Plot">'



def audio_features_trend(spotify):
    result = merge_audio_features_df(spotify)

    plt.figure(figsize=(7.5, 8), facecolor='#1ED760')
    # plt.rcParams['figure.dpi']=500

    # for feature in result['Audio Feature']:
    #     plt.plot(result.columns[1:], result[result['Audio Feature'] == feature].values.flatten()[1:], label=feature, marker='o', linewidth=3)

    for feature in result['Audio Feature']:
        values = result[result['Audio Feature'] == feature].values.flatten()[1:]
        plt.plot(result.columns[1:], values, label=feature, marker='o', linewidth=3)

        # Adding data labels
        for i, value in enumerate(values):
            plt.annotate(f'{value:.2f}', (i, value), textcoords="offset points", xytext=(0,7), ha='center')


    plt.title('Audio Feature Trends Over Time', fontsize=20, y=1.15)
    plt.xlabel('Time Range', fontsize=15, labelpad=15)
    plt.ylabel('Average Value', fontsize=15)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, shadow=True, title='Audio Feature')
    plt.grid(axis='y', linewidth=0.25)
    plt.tight_layout()

    # write image to static png
    plt.savefig('static/images/audio_feature_trend.png', bbox_inches='tight', dpi=300)
    
    # plt.show()
    plt.close()




# def audio_features_trend(spotify):
#     result = merge_audio_features_df(spotify)
#     # Create traces for each Audio Feature
#     traces = []
#     for feature in result['Audio Feature']:
#         trace = go.Scatter(x=result.columns[1:], y=result[result['Audio Feature'] == feature].values.flatten()[1:],
#                         mode='lines+markers', name=feature)
#         traces.append(trace)

#     # Create layout
#     layout = go.Layout(title=dict(text='Audio Feature Trends Over Time', font=dict(size=25), x=0.5, y=0.98),
#                     xaxis=dict(title='Time Range'),
#                     yaxis=dict(title='Average Value'),
#                     legend = dict(orientation = "h", xanchor = "center", x = 0.5, y=1.09, bgcolor='#E8ECF4', bordercolor='black'),
#                     height=800,
#                     width=800,
#                     paper_bgcolor='#1ED760')

#     # Create figure
#     fig = go.Figure(data=traces, layout=layout)
#     fig.update_xaxes(ticks="inside")
#     fig.update_yaxes(ticks="inside")
#     fig.update_yaxes(ticksuffix = " ")

#     # Show the plot
#     fig.show()

#     plotly_html = pio.to_html(fig, full_html=False)

#     # Save the plot to an HTML file
#     fig.write_html("templates/audio_feature_trend.html")

#     return plotly_html
#     # html_file_path = "static/images/audio_feature_trend.html"
#     # pyo.plot(fig, filename=html_file_path, auto_open=False)


# # audio_features_trend(spotify)
