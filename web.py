from flask import Flask, render_template, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import logging

app = Flask(__name__)


#_______This is all for fetching the latest channel upload and rate limiting, may eventually move this to another file, but we'll see_____________________


# Load environment variables
load_dotenv()
API_KEY = os.getenv('YOUTUBE_KEY')

#Channel Id for the Lantern Light Broadcast youtube channel 
CHANNEL_ID = 'UCdWHoNnRFvz44DgOCOKJgDw'

# Set up flask-limiter
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])  # Limits

# Caching variables
cache = {
    'video_data': None,
    'expires_at': None
}

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_latest_video():
    global cache

    # Check if cached data is still valid
    if cache['video_data'] and cache['expires_at'] > datetime.now():
        logging.info("Serving video data from cache.")
        return cache['video_data']

    # Make the API request
    logging.info("Fetching latest video from YouTube API.")
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={CHANNEL_ID}&maxResults=1&order=date&type=video&key={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract video information
        if 'items' in data and len(data['items']) > 0:
            latest_video = data['items'][0]
            video_id = latest_video['id']['videoId']
            video_title = latest_video['snippet']['title']
            published_at_raw = latest_video['snippet']['publishedAt']
            published_at = datetime.strptime(published_at_raw, "%Y-%m-%dT%H:%M:%SZ").strftime("%m/%d/%Y")

            # Update cache
            video_data = {'video_id': video_id, 'title': video_title, 'published_at': published_at}
            cache['video_data'] = video_data
            cache['expires_at'] = datetime.now() + timedelta(minutes=30)  # Cache expires after 30 minutes

            return video_data
        else:
            logging.error("No video data found in API response.")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching video data: {e}")
        return None
    
    #_____________________________________________________________________________________

@app.route('/')
@limiter.limit("10 per minute")  # Limit to 10 requests per minute per IP for this route
def home():
    video_data = get_latest_video()
    if video_data:
        return render_template('index.html', video=video_data)
    else:
        return render_template('index.html', video=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
