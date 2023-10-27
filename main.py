import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import streamlit as st
from app import top_artists
from app import top_tracks
from app import audio_features
from app import recommendations

def main():

    load_dotenv()

    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URL = os.getenv("SPOTIPY_REDIRECT_URL")

    scope = "user-library-read user-read-recently-played user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URL))

    st.set_page_config(layout="wide")

    st.title('Spotify Music Analysis')

    width=1500

    # Top Artists

    st.subheader('Top Artists - Short Term (Last 4 Weeks)')
    st.dataframe(data=top_artists.get_top_artists_short_term_df(), width=width)

    st.subheader('Top Artists - Medium Term (Last 6 Months)')
    st.dataframe(data=top_artists.get_top_artists_medium_term_df(), width=width)

    st.subheader('Top Artists - Long Term (Last Several Years)')
    st.dataframe(data=top_artists.get_top_artists_long_term_df(), width=width)

    # Top Tracks

    st.subheader('Top Tracks - Short Term (Last 4 Weeks)')
    st.dataframe(data=top_tracks.get_top_tracks_short_term_df(), width=width)

    st.subheader('Top Tracks - Medium Term (Last 6 Months)')
    st.dataframe(data=top_tracks.get_top_tracks_medium_term_df(), width=width)

    st.subheader('Top Tracks - Long Term (Last Several Years)')
    st.dataframe(data=top_tracks.get_top_tracks_long_term_df(), width=width)

    # Audio Feature Analysis of Top Tracks

    st.subheader('Audio Feature Analysis of Top Tracks (Short Term)')
    st.bar_chart(data=audio_features.get_audio_features_short_term(), x=None, y=None, color=None, width=width, height=0)

    st.subheader('Audio Feature Analysis of Top Tracks (Medium Term)')
    st.bar_chart(data=audio_features.get_audio_features_medium_term(), x=None, y=None, color=None, width=width, height=0)

    st.subheader('Audio Feature Analysis of Top Tracks (Long Term)')
    st.bar_chart(data=audio_features.get_audio_features_long_term(), x=None, y=None, color=None, width=width, height=0)

    # Song Recommendations (Artist)

    st.subheader('Song Recommendations Based on Top Artists (Short Term)')
    st.dataframe(data=recommendations.get_short_term_artist_recs(), width=width)

    st.subheader('Song Recommendations Based on Top Artists (Medium Term)')
    st.dataframe(data=recommendations.get_medium_term_artist_recs(), width=width)

    st.subheader('Song Recommendations Based on Top Artists (Long Term)')
    st.dataframe(data=recommendations.get_long_term_artist_recs(), width=width)

    # Song Recommendations (Tracks)

    st.subheader('Song Recommendations Based on Top Tracks (Short Term)')
    st.dataframe(data=recommendations.get_short_term_track_recs(), width=width)

    st.subheader('Song Recommendations Based on Top Tracks (Medium Term)')
    st.dataframe(data=recommendations.get_medium_term_track_recs(), width=width)

    st.subheader('Song Recommendations Based on Top Tracks (Long Term)')
    st.dataframe(data=recommendations.get_long_term_track_recs(), width=width)

if __name__ == '__main__':
    main()