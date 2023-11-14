import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from src import top_artists
from src import top_tracks
from src import audio_features
from src import recommendations
from src import current_track
from src import recently_played_tracks

def main():

    load_dotenv()

    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

    scope = "user-library-read user-read-recently-played user-top-read"

    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))

    print('\nSpotify Project\n')

    # Current Track

    print('='*150,'\n')

    print('Current Track\n')

    track = spotify.current_user_playing_track()

    if not track is None:
        print(current_track.get_current_track(spotify))
    else:
        print("No track currently playing.\n")

    # Most Recently Played Tracks

    print('='*150,'\n')

    print('Most Recently Played Tracks\n')
    print(recently_played_tracks.most_recently_played_tracks(spotify),'\n')

    # Top Artists

    print('='*150,'\n')

    print('Top Artists - Short Term (Last 4 Weeks)\n')
    print(top_artists.get_top_artists_short_term_df(spotify),'\n')

    print('Top Artists - Medium Term (Last 6 Months)\n')
    print(top_artists.get_top_artists_medium_term_df(spotify),'\n')

    print('Top Artists - Long Term (Last Several Years)\n')
    print(top_artists.get_top_artists_long_term_df(spotify),'\n')

    # Top Tracks

    print('='*150,'\n')

    print('Top Tracks - Short Term (Last 4 Weeks)\n')
    print(top_tracks.get_top_tracks_short_term_df(spotify),'\n')

    print('Top Tracks - Medium Term (Last 6 Months)\n')
    print(top_tracks.get_top_tracks_medium_term_df(spotify),'\n')

    print('Top Tracks - Long Term (Last Several Years)\n')
    print(top_tracks.get_top_tracks_long_term_df(spotify),'\n')

    # Audio Feature Analysis of Top Tracks

    print('='*150,'\n')

    print('Audio Feature Analysis of Top Tracks (Short Term)\n')
    print(audio_features.get_audio_features_short_term(spotify),'\n')

    print('Audio Feature Analysis of Top Tracks (Medium Term)\n')
    print(audio_features.get_audio_features_medium_term(spotify),'\n')

    print('Audio Feature Analysis of Top Tracks (Long Term)\n')
    print(audio_features.get_audio_features_long_term(spotify),'\n')

    # Song Recommendations (Artist)

    print('='*150,'\n')

    print('Song Recommendations Based on Top Artists (Short Term)\n')
    print(recommendations.get_short_term_artist_recs(spotify),'\n')

    print('Song Recommendations Based on Top Artists (Medium Term)\n')
    print(recommendations.get_medium_term_artist_recs(spotify),'\n')

    print('Song Recommendations Based on Top Artists (Long Term)\n')
    print(recommendations.get_long_term_artist_recs(spotify),'\n')

    # Song Recommendations (Tracks)

    print('='*150,'\n')

    print('Song Recommendations Based on Top Tracks (Short Term)\n')
    print(recommendations.get_short_term_track_recs(spotify),'\n')

    print('Song Recommendations Based on Top Tracks (Medium Term)\n')
    print(recommendations.get_medium_term_track_recs(spotify),'\n')

    print('Song Recommendations Based on Top Tracks (Long Term)\n')
    print(recommendations.get_long_term_track_recs(spotify),'\n')

if __name__ == '__main__':
    main()