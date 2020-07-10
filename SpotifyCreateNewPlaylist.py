
import json
import datetime
import requests
from datetime import timedelta
from calendar import mdays
from Secrets import spotify_token, spotify_user_id

class NewPlaylistUpdater:

    def __init__(self):
        # String representations of playlists
        self.playlist_date = PlaylistDate()

    def update_new_playlist(self):

        # Step 1: Check if "New" playlist already exixts
        playlist_id = self.check_new_playlist()
        
        if (playlist_id is not None):
            # if it does, rename it
            self.rename_new_playlist(playlist_id)

        # Step 2: Make a new "New" playlist
        self.create_new_playlist()



    def check_new_playlist(self):
        query =  f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"    

        response = requests.get(query,
        headers={
            "Authorization" : f"Bearer {spotify_token}"
        })

        response_json = response.json()['items']

        for playlist in response_json:
            if playlist['name'].lower() == 'new':
                return playlist['id']

        return None

    def create_new_playlist(self):

        query = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"

        date = self.playlist_date.new_playlist_month

        request_body = json.dumps({
            "name": "New",
            "description": f"New Songs for {date}",
            "public": True
        })

        response = requests.post(query, headers={
             "Content-Type": "application/json",
             "Authorization" : f"Bearer {spotify_token}"
        }, data=request_body)


    def rename_new_playlist(self, playlist_id):

        query = f"https://api.spotify.com/v1/playlists/{playlist_id}"

        date = self.playlist_date.renamed_playlist_month

        request_body = json.dumps({
            "name": f"{date}",
            "description": f"Memories from {date}",
        })
        
        response = requests.put(query, headers={
             "Content-Type": "application/json",
             "Authorization" : f"Bearer {spotify_token}"
        }, data=request_body)

   

class PlaylistDate:

    def __init__(self):
        self.new_playlist_month = self.get_new_playlist_date()
        self.renamed_playlist_month = self.get_renamed_playlist_date()

    def get_current_month(self):
        current_date = datetime.datetime.now()
        return current_date

    def get_next_month(self):
        current_date = self.get_current_month()
        next_month = current_date + timedelta(mdays[current_date.month])
        return next_month

    def get_prev_month(self):
        current_date = self.get_current_month()
        prev_month = current_date - timedelta(mdays[current_date.month])
        return prev_month

    def monthToString(self, date):
        date_str = date.strftime("%B %Y")
        return date_str

    def get_new_playlist_date(self):
        return self.monthToString(self.get_current_month())

    def get_renamed_playlist_date(self):
        return self.monthToString(self.get_prev_month())


    

    
if __name__ == "__main__":
    npu = NewPlaylistUpdater()
    npu.update_new_playlist()