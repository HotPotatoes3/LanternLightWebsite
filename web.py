from flask import Flask, request, render_template, abort
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('YOUTUBE_KEY')
CHANNEL_ID = 'UCdWHoNnRFvz44DgOCOKJgDw'

def get_latest_video():
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={CHANNEL_ID}&maxResults=1&order=date&type=video&key={API_KEY}'
    response = requests.get(url).json()

    if 'items' in response and len(response['items']) > 0:
        latest_video = response['items'][0]
        video_id = latest_video['id']['videoId']
        video_title = latest_video['snippet']['title']
        video_date = latest_video['snippet']['publishedAt']
        return {'video_id': video_id, 'title': video_title, 'published_at': video_date}

@app.route('/')
def home():
    video_data = get_latest_video()
    return render_template('index.html', video = video_data)  # `index.html` exists in the templates folder

'''
@app.before_request
def force_host():
    # Allowed hosts: Add any additional domains or subdomains here
    allowed_hosts

'''

if __name__ == '__main__':
    # Bind to 0.0.0.0 to make the server accessible on all network interfaces
    app.run(host="0.0.0.0", port=5000)
