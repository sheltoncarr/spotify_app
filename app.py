# This file is an example for letting any user sign in through their Spotify account

# https://community.spotify.com/t5/Spotify-for-Developers/403-User-not-approved-for-app/td-p/5214947

# https://developer.spotify.com/blog/2021-05-27-improving-the-developer-and-user-experience-for-third-party-apps

# https://developer.spotify.com/documentation/web-api/concepts/quota-modes

"""
Prerequisites

    pip3 install spotipy Flask Flask-Session

    // from your [app settings](https://developer.spotify.com/dashboard/applications)
    export SPOTIPY_CLIENT_ID='*****'
    export SPOTIPY_CLIENT_SECRET='*****'
    export SPOTIPY_REDIRECT_URL='*****' // must contain a port
    // SPOTIPY_REDIRECT_URL must be added to your [app settings](https://developer.spotify.com/dashboard/applications)
    OPTIONAL
    // in development environment for debug output
    export FLASK_ENV=development
    // so that you can invoke the app outside of the file's directory include
    export FLASK_APP=/path/to/spotipy/examples/app.py

    // on Windows, use `SET` instead of `export`

Run app.py

    python3 app.py OR python3 -m flask run
    NOTE: If receiving "port already in use" error, try other ports: 5000, 8090, 8888, etc...
        (will need to be updated in your Spotify app and SPOTIPY_REDIRECT_URL variable)
"""

import os
from flask import Flask, session, request, redirect, render_template
from flask_session import Session
import spotipy
import pandas as pd
# from dotenv import load_dotenv
from src import top_artists
from src import top_tracks
from src import audio_features
from src import recommendations
from src import current_track
from src import recently_played_tracks
from src import popularity
from src import top_genres

# load_dotenv()

# SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
# print(SPOTIPY_REDIRECT_URL)
# ^ why is this pulling https?
SPOTIPY_REDIRECT_URI = 'http://localhost:8888'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)


@app.route('/')
def index():

    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing playlist-modify-private user-library-read user-read-recently-played user-top-read',
                                               cache_handler=cache_handler,
                                               show_dialog=True, redirect_uri=SPOTIPY_REDIRECT_URI)

    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        auth_manager.get_access_token(request.args.get("code"))
        print('in auth section')
        return redirect('/')
    

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        print("We're in the sign in section")
        return render_template('sign_in.html',url=auth_url)



    # Step 3. Signed in, display data
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    global user_name
    user_name = spotify.me()["display_name"]
    print('Got here to render seciton')
    return render_template('index.html',user_name=user_name,dataEvent='Your data:')
    

@app.route('/guest')
def guest_index():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing playlist-modify-private user-library-read user-read-recently-played user-top-read',
                                               cache_handler=cache_handler,
                                               show_dialog=True,
                                               redirect_uri=SPOTIPY_REDIRECT_URI)
    user_name = 'Guest'
    return render_template('index.html',user_name=user_name)

@app.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')


# @app.route('/current_user')
# def current_user():
#     cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
#     auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
#     if not auth_manager.validate_token(cache_handler.get_cached_token()):
#         return redirect('/')
#     spotify = spotipy.Spotify(auth_manager=auth_manager)
#     return spotify.current_user()


# @app.route('/currently_playing')
# def get_currently_playing():
#     cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
#     auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
#     if not auth_manager.validate_token(cache_handler.get_cached_token()):
#         return redirect('/')
    
#     spotify = spotipy.Spotify(auth_manager=auth_manager)

#     track = spotify.current_user_playing_track()

#     if not track is None:
#         df = current_track.get_current_track(spotify)
#         title = 'Currently Playing'
#         return render_template('index.html',tables=[df.to_html(classes='data',justify='center')],titles=['Currently Playing'],
#                                                 user_name=user_name,dataEvent=title)
#     return "No track currently playing."


@app.route('/most_recent_tracks')
def get_most_recent_tracks():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df = recently_played_tracks.most_recently_played_tracks(spotify)
    title = 'Most Recent Tracks:'
    
    return render_template('index.html',tables=[df.to_html(classes='data',justify='center')],titles=['Most Recent Tracks'],
                                                user_name=user_name,dataEvent=title)


@app.route('/top_artists')
def get_top_artists():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    print(request.url_rule)
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df1 = top_artists.get_top_artists_short_term_df(spotify)
    df2 = top_artists.get_top_artists_medium_term_df(spotify)
    df3 = top_artists.get_top_artists_long_term_df(spotify)
    title = 'Your Top Artists:'
    

    return render_template('index.html',tables=[df1.to_html(classes='data',justify='center'),df2.to_html(classes='data',justify='center'),
                                                df3.to_html(classes='data',justify='center')],titles=['Short Term','Medium Term','Long Term'],
                                                user_name=user_name,dataEvent=title)


@app.route('/top_tracks')
def get_top_tracks():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df1 = top_tracks.get_top_tracks_short_term_df(spotify)
    df2 = top_tracks.get_top_tracks_medium_term_df(spotify)
    df3 = top_tracks.get_top_tracks_long_term_df(spotify)
    title = 'Your Top Tracks:'

    return render_template('index.html',tables=[df1.to_html(classes='data',justify='center'),df2.to_html(classes='data',justify='center'),
                                                df3.to_html(classes='data',justify='center')],titles=['Short Term','Medium Term','Long Term'],
                                                user_name=user_name,dataEvent=title)


@app.route('/top_genres')
def get_top_genres():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df1 = top_genres.get_top_genres_short_term_df(spotify)
    df2 = top_genres.get_top_genres_medium_term_df(spotify)
    df3 = top_genres.get_top_genres_long_term_df(spotify)
    title = 'Your Top Genres:'

    return render_template('index.html',tables=[df1.to_html(classes='data',justify='center'),df2.to_html(classes='data',justify='center'),
                                                df3.to_html(classes='data',justify='center')],titles=['Short Term','Medium Term','Long Term'],
                                                user_name=user_name,dataEvent=title)


@app.route('/audio_features')
def get_features():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df1 = audio_features.get_audio_features_short_term(spotify)
    df2 = audio_features.get_audio_features_medium_term(spotify)
    df3 = audio_features.get_audio_features_long_term(spotify)
    title = 'Your Audio Features:'

    return render_template('index.html',tables=[df1.to_html(classes='data',justify='center'),df2.to_html(classes='data',justify='center'),
                                                df3.to_html(classes='data',justify='center')],titles=['Short Term','Medium Term','Long Term'],
                                                user_name=user_name,dataEvent=title)


@app.route('/recommendations')
def get_recommendations():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df1 = recommendations.get_short_term_track_recs(spotify)
    df2 = recommendations.get_medium_term_track_recs(spotify)
    df3 = recommendations.get_long_term_track_recs(spotify)
    df4 = recommendations.get_short_term_artist_recs(spotify)
    df5 = recommendations.get_medium_term_artist_recs(spotify)
    df6 = recommendations.get_long_term_artist_recs(spotify)
    title = 'Your Top Recommendations:'

    return render_template('index.html',tables=[df1.to_html(classes='data',justify='center'),df2.to_html(classes='data',justify='center'),
                                                df3.to_html(classes='data',justify='center'),df4.to_html(classes='data',justify='center'),
                                                df5.to_html(classes='data',justify='center'),df6.to_html(classes='data',justify='center')],
                                                titles=['Based on Top Tracks (Short Term)','Based on Top Tracks (Medium Term)','Based on Top Tracks (Long Term)',
                                                        'Based on Top Artists (Short Term)','Based on Top Artists (Medium Term)','Based on Top Artists (Long Term)'],
                                                user_name=user_name,dataEvent=title)


@app.route('/popularity')
def get_popularity():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    df1 = popularity.get_top_artists_short_term_popularity_df(spotify)
    df2 = popularity.get_top_artists_medium_term_popularity_df(spotify)
    df3 = popularity.get_top_artists_long_term_popularity_df(spotify)
    title = 'Popularity of Your Top Artists (Sorted by Popularity):'

    return render_template('index.html',tables=[df1.to_html(classes='data',justify='center'),df2.to_html(classes='data',justify='center'),
                                                df3.to_html(classes='data',justify='center')],titles=['Short Term','Medium Term','Long Term'],
                                                user_name=user_name,dataEvent=title)


@app.route('/about_us')
def about_us():
    return render_template('about.html')

@app.route('/your_data')
def user_data():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, redirect_uri=SPOTIPY_REDIRECT_URI)
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    # user name
    user_name = spotify.me()["display_name"]

    # follower count
    follower_count = spotify.me()["followers"]["total"]

    list_of_playlists = spotify.current_user_playlists()["items"]
    # total number of playlists
    playlists = len(list_of_playlists)

    # number of collaborative playlists
    collaborative_playlists = 0
    for idx in range(len(list_of_playlists)):
        if not list_of_playlists[idx]["collaborative"] is False:
            collaborative_playlists += 1
    
    # number of playlists owned by the user
    owned_playlists = 0
    for idx in range(len(list_of_playlists)):
        if list_of_playlists[idx]["owner"]["display_name"] == user_name:
            owned_playlists += 1

    hold = "It's coming"

    # currently playing
    track = spotify.current_user_playing_track()
    if not track is None:
        result = spotify.current_user_playing_track()
        track_title = result['item']['name']
        artist_list = ', '.join(artist['name'] for artist in result['item']['artists'])
        current_song = track_title + ' by ' + artist_list
    if track is None:
        current_song = 'No song is playing'

    return render_template('user_data.html',user_name=user_name,follower_count=follower_count,
                           playlist_count=playlists,collaborative_playlists=collaborative_playlists,
                           owned_playlists=owned_playlists,hold=hold,current_song=current_song)


@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')


'''
Following lines allow application to be run more conveniently with
`python app.py` (Make sure you're using python3)
(Also includes directive to leverage pythons threading capacity.)
'''
if __name__ == '__main__':
    app.run(threaded=True, port=8888)