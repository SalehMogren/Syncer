import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import requests
import youtube_dl

# from exceptions import ResponseException
# from secrets import spotify_token, spotify_user_id


class Track:

    def __init__(self, name, artist, sp_id, yt_id, playlist_id):
        self.name = name
        self.artist = artist
        self.sp_id = sp_id
        self.yt_id = yt_id
        self.playlist_id = playlist_id

    # exist spotify track
    def is_spotify(self):
        return self.sp_id != None

    def is_youtube(self):
        return self.yt_id != None
    # add track to spotify

    def is_synced(self):
        return self.is_spotify() and self.is_youtube()

    def add_to_spotify(self, sp_id):
        pass

    # add track to youtube playlist
    def add_to_youtube(self, yt_id):
        pass


class Playlist:
    tracks = {Track}

    def __init__(self, name, sp_id, yt_id):
        self.sp_id = sp_id
        self.yt_id = yt_id
        self.name = name
        if sp_id:
            self.fetch_spotify_tracks()
        if yt_id:
            self.fetch_youtube_tracks()

    # add yt or sp ids to playlist

    def connect_platform(self, sp_id, yt_id):
        if sp_id:
            self.sp_id = sp_id
            self.fetch_spotify_tracks()
        if yt_id:
            self.yt_id = yt_id
            self.fetch_youtube_tracks()

    def search_track(self, track_name, artist_name) -> str:
        """
        match a track by name and artist 

        Arguemnts:
            track_name {string} -- Track Name
            artist_name {string} -- Artist Name
        """
        for track in self.tracks:
            if track.name == track_name and track.artist == artist_name:
                return track
        return "Not found"

    # retreive spotify tracks

    def fetch_spotify_tracks(self, sp_id):
        tracks = [Track]
        reponse_items = []
        for item in reponse_items:
            if self.tracks[item.name]:
                self.tracks[item.name].add_to_spotify(item.id)
            else:
                self.tracks[item.name] = Track(
                    name=item.name, artist=item.artist, sp_id=item.id)
        return tracks

    def fetch_youtube_tracks(yt_id):
        tracks = [Track]
        return tracks


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    playlists = {}

    # Getting youtube playlist
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        maxResults=25,
        mine=True
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
