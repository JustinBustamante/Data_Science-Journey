from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from textblob import TextBlob

# Initialize YouTube API
def youtube_service(api_key):
    try:
        return build('youtube', 'v3', developerKey=api_key)
    except HttpError as e:
        print(f"An HTTP error occurred: {e.resp.status} {e.content}")
        return None

# Function to get comments
def get_comments(youtube, video_id, max_results=100):
    comments = []
    try:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results,
            textFormat='plainText'
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

    except HttpError as e:
        print(f"An HTTP error occurred: {e.resp.status} {e.content}")

    return comments

# Function for sentiment analysis
def analyze_sentiment(comments, threshold=0.2):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    
    for comment in comments:
        try:
            analysis = TextBlob(comment)
            if analysis.sentiment.polarity > threshold:
                sentiments['positive'] += 1
            elif analysis.sentiment.polarity < -threshold:
                sentiments['negative'] += 1
            else:
                sentiments['neutral'] += 1
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")

    return sentiments

# Main function
def main(api_key, video_url):
    youtube = youtube_service(api_key)
    if youtube:
        video_id = video_url.split('v=')[1]  # Extract video ID from URL
        comments = get_comments(youtube, video_id)
        if comments:
            sentiments = analyze_sentiment(comments)
            print(sentiments)
        else:
            print("No comments found or error occurred.")
    else:
        print("Failed to initialize YouTube service.")

# Replace YOUR_API_KEY with your actual YouTube API Key
api_key = 'YOUR_API_KEY'
video_url = 'https://www.youtube.com/watch?v=XXXXX'  # Replace with your video URL
main(api_key, video_url)
