import pandas as pd
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotipy.oauth2 import SpotifyOAuth
# import os
# from dotenv import load_dotenv
# from src import top_tracks

# load_dotenv()

# SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
# SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

# scope = "user-library-read user-read-recently-played user-top-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))

def audio_feature_meaning():
    audio_feature = ['Danceability','Energy','Mode','Speechiness','Acousticness','Instrumentalness','Liveness','Valence']
    description = ['Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.',
                   'Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.',
                   'Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.',
                   'Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.',
                   'A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.',
                   'Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.',
                   'Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.',
                   'A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).'
                  ]

    df = pd.DataFrame({
        'Audio Feature': audio_feature,
        'Description': description
    })

    df.index += 1
    return df


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


# =================================================================================

# def get_audio_features_short_term(spotify, limit=50, time_range='short_term'):
#     results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
#     tracks = [item['name'] for item in results['items']]
#     artists = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]

#     track_uri = []

#     for i in range(limit):
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=tracks[i],artist=artists[i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])


#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df


# def get_audio_features_medium_term(spotify, limit=50, time_range='medium_term'):
#     results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
#     tracks = [item['name'] for item in results['items']]
#     artists = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]

#     track_uri = []

#     for i in range(limit):
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=tracks[i],artist=artists[i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])


#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df


# def get_audio_features_long_term(spotify, limit=50, time_range='long_term'):
#     results = spotify.current_user_top_tracks(limit=limit, time_range=time_range)
#     tracks = [item['name'] for item in results['items']]
#     artists = [', '.join(artist['name'] for artist in item['artists']) for item in results['items']]

#     track_uri = []

#     for i in range(limit):
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=tracks[i],artist=artists[i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])


#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df

#==================================================================

# # Get Audio Features of top tracks (short term)

# def get_audio_features_short_term(spotify):
#     top_short_term_tracks_df = top_tracks.get_top_tracks_short_term_df(spotify)
#     top_tracks_af = top_short_term_tracks_df[['Track', 'Artist']].reset_index()

#     track_uri = []

#     for i in top_tracks_af.index:
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_tracks_af['Track'][i],artist=top_tracks_af['Artist'][i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])

#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df


# # Get Audio Features of top tracks (medium term)

# def get_audio_features_medium_term(spotify):
#     top_medium_term_tracks_df = top_tracks.get_top_tracks_medium_term_df(spotify)
#     top_tracks_af = top_medium_term_tracks_df[['Track', 'Artist']].reset_index()

#     track_uri = []

#     for i in top_tracks_af.index:
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_tracks_af['Track'][i],artist=top_tracks_af['Artist'][i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])

#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df


# # Get Audio Features of top tracks (long term)

# def get_audio_features_long_term(spotify):
#     top_long_term_tracks_df = top_tracks.get_top_tracks_long_term_df(spotify)
#     top_tracks_af = top_long_term_tracks_df[['Track', 'Artist']].reset_index()

#     track_uri = []

#     for i in top_tracks_af.index:
#         search_results = spotify.search(q='track:{track} artist:{artist}'.format(track=top_tracks_af['Track'][i],artist=top_tracks_af['Artist'][i]), type='track')
#         if search_results['tracks']['items'] == []:
#             continue
#         track_uri.append(search_results['tracks']['items'][0]['uri'])

#     df = pd.DataFrame(spotify.audio_features(tracks=track_uri))
#     df.index +=1
#     drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'duration_ms', 'time_signature', 'loudness']
#     df = df.drop(columns=drop_columns)
#     df = df.mean(axis=0)
#     df = pd.DataFrame({'Feature':df.index, 'Value':df.values})
#     return df