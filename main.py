from youtube_transcript_api import YouTubeTranscriptApi
import os

# Create a directory to store the transcripts
if not os.path.exists("transcripts"):
    os.makedirs("transcripts")

# List of YouTube video URLs
video_urls = [
    "https://www.youtube.com/watch?v=eX2qFMC8cFo",
    "https://www.youtube.com/watch?v=b-iS_2_n-O4",
    "https://www.youtube.com/watch?v=sBswZ3gS_I8",
    "https://www.youtube.com/watch?v=1waHlpKiNyY",
    "https://www.youtube.com/watch?v=S1_p7_W7i-c",
    "https://www.youtube.com/watch?v=J8Eh7-UvcCM",
    "https://www.youtube.com/watch?v=8A2t_tAjMz8",
    "https://www.youtube.com/watch?v=p1-fiq1a2iA",
    "https://www.youtube.com/watch?v=1gDhl4leEzA",
    "https://www.youtube.com/watch?v=XGf2GcyHPhc"
]

for url in video_urls:
    try:
        video_id = url.split("=")[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Use video_id for the filename, which is unique and safe for filenames.
        file_path = os.path.join("transcripts", f"{video_id}.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            for item in transcript_list:
                f.write(f"{item['text']}\n")
        print(f"Transcript for video ID '{video_id}' saved to {file_path}")

    except Exception as e:
        print(f"Could not retrieve transcript for {url}: {e}")