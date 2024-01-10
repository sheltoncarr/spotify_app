import os
from flask import Flask, session, request, redirect, render_template
from flask_session import Session
import spotipy
import pandas as pd
import statistics as stats
from dotenv import load_dotenv
from src import top_artists
from src import top_tracks
from src import audio_features
from src import recommendations
from src import recently_played_tracks
from src import popularity
from src import top_genres
from src import top_years
from src import audio_features_trend
from src import top_years_bar_chart
from src import top_genres_bar_chart

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

@app.route('/')
def index():
    global cache_handler
    global auth_manager
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing playlist-modify-private user-library-read user-read-recently-played user-top-read playlist-read-private playlist-read-collaborative',
                                               cache_handler=cache_handler,
                                               show_dialog=True, redirect_uri=SPOTIPY_REDIRECT_URL)

    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')
    

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return render_template('sign_in.html',url=auth_url)

    # Step 3. Signed in, display data
    global spotify
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return redirect('/home')


@app.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')

@app.route('/home')
def home_page():
    global user_name
    user_name = spotify.me()["display_name"]
    artist_results = spotify.current_user_top_artists(limit=50, time_range='long_term')
    artist_list = [item['name'] for item in artist_results['items']]
    top_artist = artist_list[0]
    popularity_list = [item['popularity'] for item in artist_results['items']]
    df_artist = pd.DataFrame({'Artist': artist_list, "Popularity (Out of 100)": popularity_list})
    df_artist.sort_values(by=["Popularity (Out of 100)"], inplace=True, ascending=False)
    df_artist.reset_index(drop=True,inplace=True)
    top_pop = df_artist.loc[0].iat[0]
    top_niche = df_artist.loc[49].iat[0]
    track_results = spotify.current_user_top_tracks(limit=1, time_range='long_term')
    top_track = track_results['items'][0]['name']
    top_track_artist = track_results['items'][0]['artists'][0]['name']
    track_uri_list = [item['id'] for item in track_results['items']]
    df_dur = pd.DataFrame(spotify.audio_features(tracks=track_uri_list))
    drop_columns = ['type','id','uri','track_href','analysis_url', 'key', 'tempo', 'time_signature', 'loudness']
    df_dur = df_dur.drop(columns=drop_columns)
    df_dur = df_dur.mean(axis=0)
    df_dur = pd.DataFrame({'Audio Feature':df_dur.index, 'Average Value':df_dur.values})
    minutes, seconds = divmod(int(df_dur.loc[8].iat[1]/1000), 60)
    duration = str(minutes) + ' minutes and ' + str(seconds) + ' seconds'
    top_genre = top_genres.get_top_genres_long_term_df(spotify).loc[1].iat[0]
    top_year  = top_years.get_top_years_long_term_df(spotify).loc[1].iat[0]
    

    return render_template('home.html', user_name=user_name, 
                           top_artist=top_artist,
                           top_track=top_track,
                           top_track_artist=top_track_artist,
                           duration=duration,
                           top_genre=top_genre,
                           top_year=top_year,
                           top_pop=top_pop,
                           top_niche=top_niche)



@app.route('/most_recent_tracks')
def get_most_recent_tracks():

    df1 = recently_played_tracks.most_recently_played_tracks(spotify)
    title = 'Your Most Recent Tracks:'
    
    tables = [
        {'title': 'Most Recent Tracks', 'data': df1, 'id':'table1'}
    ]

    return render_template('index.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/top_artists')
def get_top_artists():

    df1 = top_artists.get_top_artists_short_term_df(spotify)
    df2 = top_artists.get_top_artists_medium_term_df(spotify)
    df3 = top_artists.get_top_artists_long_term_df(spotify)
    title = 'Your Top Artists:'

    tables = [
        {'title': 'Short Term (Last 4 Weeks)', 'data': df1, 'id':'table1'},
        {'title': 'Medium Term (Last 6 Months)', 'data': df2,'id':'table2'},
        {'title': 'Long Term (Last Several Years)', 'data': df3,'id':'table3'},
    ]

    return render_template('index.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/top_tracks')
def get_top_tracks():

    df1 = top_tracks.get_top_tracks_short_term_df(spotify)
    df2 = top_tracks.get_top_tracks_medium_term_df(spotify)
    df3 = top_tracks.get_top_tracks_long_term_df(spotify)
    title = 'Your Top Tracks:'

    tables = [
        {'title': 'Short Term (Last 4 Weeks)', 'data': df1, 'id':'table1'},
        {'title': 'Medium Term (Last 6 Months)', 'data': df2,'id':'table2'},
        {'title': 'Long Term (Last Several Years)', 'data': df3,'id':'table3'},
    ]

    return render_template('index.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/top_genres')
def get_top_genres():

    df1 = top_genres.get_top_genres_short_term_df(spotify)
    df2 = top_genres.get_top_genres_medium_term_df(spotify)
    df3 = top_genres.get_top_genres_long_term_df(spotify)
    title = 'Your Top Genres:'

    tables = [
        {'title': 'Short Term (Last 4 Weeks)', 'data': df1, 'id':'table1'},
        {'title': 'Medium Term (Last 6 Months)', 'data': df2,'id':'table2'},
        {'title': 'Long Term (Last Several Years)', 'data': df3,'id':'table3'},
    ]

    return render_template('index.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/top_genres_bar_chart')
def top_genres_visual():
    top_genres_bar_chart.top_genres_bar_chart(spotify)
    title = 'Your Top Genres:'

    return render_template("top_genres_bar_chart.html", user_name=user_name, dataEvent=title)


@app.route('/top_years')
def get_top_years():

    df1 = top_years.get_top_years_short_term_df(spotify)
    df2 = top_years.get_top_years_medium_term_df(spotify)
    df3 = top_years.get_top_years_long_term_df(spotify)
    title = 'Your Top Years:'
    length = df1.size

    tables = [
        {'title': 'Short Term (Last 4 Weeks)', 'data': df1, 'id':'table1'},
        {'title': 'Medium Term (Last 6 Months)', 'data': df2,'id':'table2'},
        {'title': 'Long Term (Last Several Years)', 'data': df3,'id':'table3'},
    ]

    return render_template('graph_data.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/top_years_bar_chart')
def top_years_visual():
    top_years_bar_chart.top_years_bar_chart(spotify)
    title = 'Your Top Years (based on release year):'

    return render_template("top_years_bar_chart.html", user_name=user_name, dataEvent=title)


@app.route('/audio_features')
def get_features():

    df = audio_features.audio_feature_meaning()
    df1 = audio_features.get_audio_features_short_term(spotify)
    df2 = audio_features.get_audio_features_medium_term(spotify)
    df3 = audio_features.get_audio_features_long_term(spotify)
    title = 'Your Audio Features:'

    tables = [
        {'title': 'Audio Feature Definitions', 'data': df, 'id':'table1'},
        {'title': 'Short Term (Last 4 Weeks)', 'data': df1, 'id':'table2'},
        {'title': 'Medium Term (Last 6 Months)', 'data': df2,'id':'table3'},
        {'title': 'Long Term (Last Several Years)', 'data': df3,'id':'table4'},
    ]

    return render_template('graph_data.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/audio_features_trend')
def audio_features_trend_visual():
    audio_features_trend.audio_features_trend(spotify)
    df = audio_features.audio_feature_meaning()
    title = 'Your Audio Features:'

    tables = [
        {'title': 'Audio Feature Definitions', 'data': df, 'id':'table1'}
    ]
    return render_template("audio_features_trend.html", tables=tables, user_name=user_name, dataEvent=title)


@app.route('/recommendations')
def get_recommendations():

    df1 = recommendations.get_short_term_track_recs(spotify)
    df2 = recommendations.get_medium_term_track_recs(spotify)
    df3 = recommendations.get_long_term_track_recs(spotify)
    df4 = recommendations.get_short_term_artist_recs(spotify)
    df5 = recommendations.get_medium_term_artist_recs(spotify)
    df6 = recommendations.get_long_term_artist_recs(spotify)
    title = 'Your Recommendations: (Refresh for new recs)'

    tables = [
        {'title': 'Based on Top Tracks (Short Term)', 'data': df1, 'id':'table1'},
        {'title': 'Based on Top Tracks (Medium Term)', 'data': df2,'id':'table2'},
        {'title': 'Based on Top Tracks (Long Term)', 'data': df3,'id':'table3'},
        {'title': 'Based on Top Artists (Short Term)', 'data': df4, 'id':'table4'},
        {'title': 'Based on Top Artists (Medium Term)', 'data': df5,'id':'table5'},
        {'title': 'Based on Top Artists (Long Term)', 'data': df6,'id':'table6'},
    ]

    return render_template('graph_data.html', tables=tables, user_name=user_name, dataEvent=title)


@app.route('/popularity')
def get_popularity():

    df1 = popularity.get_top_artists_short_term_popularity_df(spotify)
    df2 = popularity.get_top_artists_medium_term_popularity_df(spotify)
    df3 = popularity.get_top_artists_long_term_popularity_df(spotify)
    title = 'Popularity of Your Top Artists (Sorted by Popularity):'


    tables = [
        {'title': 'Short Term (Last 4 Weeks)', 'data': df1, 'id':'table1'},
        {'title': 'Medium Term (Last 6 Months)', 'data': df2,'id':'table2'},
        {'title': 'Long Term (Last Several Years)', 'data': df3,'id':'table3'},
    ]

    return render_template('index.html', tables=tables, user_name=user_name, dataEvent=title)




@app.route('/about_us')
def about_us():
    return render_template('about.html')

@app.route('/your_data')
def user_data():
    
    user_info = spotify.me()
    user_name = user_info["display_name"]
    if len(user_info['images'])>0:
        profile_pic = user_info['images'][1]['url']
    else: 
        profile_pic = ''

    # follower count
    follower_count = user_info["followers"]["total"]

    response = spotify.current_user_playlists()
    list_of_playlists = response["items"]

    while response["next"]:
        response = spotify.next(response)
        list_of_playlists.extend(response["items"])

    # total number of playlists
    playlists_num = len(list_of_playlists)
    
    # number of playlists owned by the user
    owned_playlists = 0
    for idx in range(playlists_num):
        if list_of_playlists[idx]["owner"]["display_name"] == user_name:
            owned_playlists += 1
    per_user_owned = int((owned_playlists/playlists_num)*100)

    # number of playlists owned by spotify
    spot_playlists = 0
    for idx in range(playlists_num):
        if list_of_playlists[idx]["owner"]["display_name"] == 'Spotify':
            spot_playlists += 1
    per_spot_owned = int((spot_playlists/playlists_num)*100)

    # number of playlists owned by other users
    other_user_playlists = 0
    other_user_names = []
    for idx in range(playlists_num):
        if list_of_playlists[idx]["owner"]["display_name"] != 'Spotify':
            if list_of_playlists[idx]["owner"]["display_name"] != user_name:
                other_user_playlists += 1
                other_user_names.append(list_of_playlists[idx]["owner"]["display_name"])
    per_other_user_owned = int((other_user_playlists/playlists_num)*100)
    other_user_followed = stats.mode(other_user_names)
    
    # number of collaborative playlists
    collaborative_playlists = 0
    for idx in range(playlists_num):
        if list_of_playlists[idx]["collaborative"] != False:
            collaborative_playlists += 1

    # number of public playlists
    public_playlists = 0
    for idx in range(playlists_num):
        if list_of_playlists[idx]["public"] == True:
            public_playlists += 1

    # currently playing
    track = spotify.current_user_playing_track()
    if not track is None:
        track_title = track['item']['name']
        artist_list = ', '.join(artist['name'] for artist in track['item']['artists'])
        current_song = track_title + ' by ' + artist_list
    if track is None:
        current_song = 'No song is playing'

    # avg number of songs per playlist
    track_counts = []
    for idx in range(playlists_num):
        track_counts.append(list_of_playlists[idx]["tracks"]["total"])
    avg_track_count = int(stats.fmean(track_counts))

    # longest playlist
    track_counts.sort()
    long_playlist = track_counts[len(track_counts)-1]

    # shortest playlist
    short_playlist = track_counts[0]


    return render_template('user_data.html',user_name=user_name,
                           profile_pic=profile_pic,
                           follower_count=follower_count,
                           playlist_count=playlists_num,
                           owned_playlists=owned_playlists,
                           per_user_owned=per_user_owned,
                           spot_playlists=spot_playlists,
                           per_spot_owned=per_spot_owned,
                           collaborative_playlists=collaborative_playlists,
                           other_user_playlists=other_user_playlists,
                           other_user_followed=other_user_followed,
                           per_other_user_owned=per_other_user_owned,
                           current_song=current_song,
                           public_playlists=public_playlists,
                           avg_track_count=avg_track_count,
                           long_playlist=long_playlist,
                           short_playlist=short_playlist)


if __name__ == '__main__':
    app.run(threaded=True, port=8888)
