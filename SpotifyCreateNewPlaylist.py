
import json
import datetime
import requests
from datetime import timedelta
from calendar import mdays
from Secrets import spotify_token, spotify_user_id

"""
When script is run, it looks for a "New" playlist,
if it doesn't exists then it makes a new one, else it renames it to the month and year
and creates a new "New" playlist 
"""

class NewPlaylistUpdater:

    def __init__(self):
        pass

    def update_new_playlist(self):
        # Step 1: Check if "New" playlist already exixts
        if (check_new_playlist):





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
                self.rename_new_playlist(playlist['id'])
                break

        self.create_new_playlist()        

    def create_new_playlist(self):

        query = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"

        curent_month = self.monthToString(self.get_current_month())

        request_body = json.dumps({
            "name": "New",
            "description": f"New Songs for {curent_month}",
            "public": True
        })

        response = requests.post(query, headers={
             "Content-Type": "application/json",
             "Authorization" : f"Bearer {spotify_token}"
        }, data=request_body)


    def rename_new_playlist(self, playlist_id):

        query = f"https://api.spotify.com/v1/playlists/{playlist_id}"

        current_date = self.monthToString(self.get_current_month())

        request_body = json.dumps({
            "name": f"{current_date}",
            "description": f"Memories from {current_date}",
        })
        
        response = requests.put(query, headers={
             "Content-Type": "application/json",
             "Authorization" : f"Bearer {spotify_token}"
        }, data=request_body)

   

class Date:

    def __init__:
        self.current_date = self.get_current_month()

     def get_current_month(self):
        current_date = datetime.datetime.now()
        return current_date

    def get_next_month(self):
        current_date = self.get_current_month()
        next_month = current_date + timedelta(mdays[current_date.month])
        print(self.monthToString(next_month))
        return next_month

    def monthToString(self, date):
        date_str = date.strftime("%B %Y")
        return date_str
        


if __name__ == "__main__":
    cp = CreatePlaylist()
    cp.check_new_playlist()